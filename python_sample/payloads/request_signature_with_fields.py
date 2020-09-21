import json
from .recipients import Recipients
from .cc import CC
from .merge_fields import MergeFields
import requests
from .fields_payload import FieldsPayload

type_fields = {"message": str, "name": str, "original_file_id": int, "cc": [CC], "fields_payload": [FieldsPayload],
               "merge_fields": [MergeFields], "recipients": [Recipients], "is_ordered": bool, "embedded_signing": bool}


class RequestSignaturesWithFields:
    message = ''
    cc = []
    embedded_signing = False
    merge_fields = []
    original_file_id = 0
    recipients = []
    is_ordered = False
    name = ''
    fields_payload = []

    def __init__(self, *args, **kwargs):
        mandatory_fields = ["original_file_id", "recipients", "is_ordered", "name", "fields_payload"]

        for key, val in kwargs.items():
            setattr(self, key, val)
            if key in mandatory_fields:
                mandatory_fields.remove(key)

        if mandatory_fields:
            raise Exception("{} are missing".format(','.join(mandatory_fields)))

    def __str__(self):
        resp = dict()
        resp["message"] = self.message
        resp["cc"] = [i.to_dict() for i in self.cc if isinstance(i, CC)]
        resp["embedded_signing"] = self.embedded_signing
        resp["merge_fields"] = [i.to_dict() for i in self.merge_fields if isinstance(i, MergeFields)]
        resp["original_file_id"] = self.original_file_id
        resp["fields_payload"] = [i.to_dict() for i in self.fields_payload if isinstance(i, FieldsPayload)]
        resp["recipients"] = [i.to_dict() for i in self.recipients if isinstance(i, Recipients)]
        resp['is_ordered'] = self.is_ordered
        resp["name"] = self.name
        return json.dumps(resp)

    def to_dict(self):
        resp = dict()
        resp["message"] = self.message
        resp["cc"] = [i.to_dict() for i in self.cc if isinstance(i, CC)]
        resp["original_file_id"] = self.original_file_id
        resp["embedded_signing"] = self.embedded_signing
        resp["merge_fields"] = [i.to_dict() for i in self.merge_fields if isinstance(i, MergeFields)]
        resp["fields_payload"] = [i.to_dict() for i in self.fields_payload if isinstance(i, FieldsPayload)]
        resp["recipients"] = [i.to_dict() for i in self.recipients if isinstance(i, Recipients)]
        resp['is_ordered'] = self.is_ordered
        resp["name"] = self.name
        return resp

    def create_signature_request(self, base_headers, base_url):
        """
        Used to create a signature request with originals
        :param base_url: string, Base URL to be pre fixed to all API
        :param base_headers: dictionary, with all the necessary tokes for transaction
        :return: tuple: json response, status code
        """
        try:
            url = base_url + "v2/rs/envelope/"

            headers = dict(base_headers)
            headers["Content-Type"] = "application/json"

            payload = self.to_dict()
            resp = requests.post(url=url, headers=headers, json=payload)
            return resp.json(), resp.status_code

        except Exception as e:
            return e, 400

    def __setattr__(self, key, value):
        if not isinstance(value, type_fields.get(key) if not isinstance(type_fields.get(key), list) else list):
            raise Exception("{} should be a {}".format(key, type_fields.get(key) if not isinstance(type_fields.get(key),
                                                                                                   list) else list))

        if isinstance(type_fields.get(key), list):
            for obj in value:
                if not isinstance(obj, type_fields.get(key)[0]):
                    raise Exception("{} should be a {}".format(key, type_fields.get(key)[0]))

        super().__setattr__(key, value)
