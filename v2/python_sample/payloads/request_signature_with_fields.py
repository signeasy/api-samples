import json
from .recipients import EnvelopeRecipients
from .cc import CC
from .merge_fields import MergeFields
import requests
from .fields_payload import EnvelopesFieldsPayload
from .originals import Originals

type_fields = {"message": str, "name": str, "originals": [Originals], "cc": [CC], "fields_payload": [EnvelopesFieldsPayload],
               "merge_fields": [MergeFields], "recipients": [EnvelopeRecipients], "is_ordered": bool, "embedded_signing": bool}


class RequestSignaturesWithFields:
    message = ''
    cc = []
    embedded_signing = False
    merge_fields = []
    originals = []
    recipients = []
    is_ordered = False
    name = ''
    fields_payload = []

    def __init__(self, *args, **kwargs):
        mandatory_fields = ["originals", "recipients", "is_ordered", "name", "fields_payload"]

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
        resp["originals"] = [i.to_dict() for i in self.originals if isinstance(i, Originals)]
        resp["fields_payload"] = [i.to_dict() for i in self.fields_payload if isinstance(i, EnvelopesFieldsPayload)]
        resp["recipients"] = [i.to_dict() for i in self.recipients if isinstance(i, EnvelopeRecipients)]
        resp['is_ordered'] = self.is_ordered
        resp["name"] = self.name
        return json.dumps(resp)

    def to_dict(self):
        resp = dict()
        resp["message"] = self.message
        resp["cc"] = [i.to_dict() for i in self.cc if isinstance(i, CC)]
        resp["originals"] = [i.to_dict() for i in self.originals if isinstance(i, Originals)]
        resp["embedded_signing"] = self.embedded_signing
        resp["merge_fields"] = [i.to_dict() for i in self.merge_fields if isinstance(i, MergeFields)]
        resp["fields_payload"] = [i.to_dict() for i in self.fields_payload if isinstance(i, EnvelopesFieldsPayload)]
        resp["recipients"] = [i.to_dict() for i in self.recipients if isinstance(i, EnvelopeRecipients)]
        resp['is_ordered'] = self.is_ordered
        resp["name"] = self.name
        return resp

    def create_signature_request(self, base_headers, base_url):
        """
        Used to create a signature request on originals
        :param base_url: string, Base URL to be pre fixed to all API
        :param base_headers: dictionary, with all the necessary tokes for transaction
        :return: tuple: json response, status code
        """
        try:
            url = base_url + "v2/rs/envelope"

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
