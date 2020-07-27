import json
from .recipients import Recipients
from .cc import CC
from .merge_fields import MergeFields
import requests


class RequestSignatures:
    message = ''
    cc = [CC]
    file_password = ''
    embedded_signing = False
    merge_fields = [MergeFields]
    template_file_id = 0
    recipients = [Recipients]
    is_ordered = False
    name = ''

    def __init__(self, *args, **kwargs):
        mandatory_fields = ["template_file_id", "recipients", "is_ordered", "name"]
        ref_obj = list()

        for key, val in kwargs.items():
            if getattr(self, key, None) is not None:
                if not isinstance(val, type(getattr(self, key, None))
                                                  if not isinstance(getattr(self, key, None), list) else list):
                    raise Exception("value for {} is not of valid type".format(key))

                if isinstance(val, list):
                    for obj in val:
                        if not isinstance(obj, getattr(self, key, None)[0]):
                            temp_obj = getattr(self, key, None)[0](**obj)
                            ref_obj.append(temp_obj)

                if ref_obj:
                    setattr(self, key, ref_obj)
                    ref_obj = list()
                else:
                    setattr(self, key, val)

                if key in mandatory_fields:
                    mandatory_fields.remove(key)

        if mandatory_fields:
            raise Exception("{} are missing".format(','.join(mandatory_fields)))

    def __str__(self):
        resp = dict()
        resp["message"] = self.message
        resp["cc"] = [i.to_dict() for i in self.cc if isinstance(i, CC)]
        resp["file_password"] = self.file_password
        resp["embedded_signing"] = self.embedded_signing
        resp["merge_fields"] = [i.to_dict() for i in self.merge_fields if isinstance(i, MergeFields)]
        resp["template_file_id"] = self.template_file_id
        resp["recipients"] = [i.to_dict() for i in self.recipients if isinstance(i, Recipients)]
        resp['is_ordered'] = self.is_ordered
        resp["name"] = self.name
        return json.dumps(resp)

    def to_dict(self):
        resp = dict()
        resp["message"] = self.message
        resp["cc"] = [i.to_dict() for i in self.cc if isinstance(i, CC)]
        resp["file_password"] = self.file_password
        resp["embedded_signing"] = self.embedded_signing
        resp["merge_fields"] = [i.to_dict() for i in self.merge_fields if isinstance(i, MergeFields)]
        resp["template_file_id"] = self.template_file_id
        resp["recipients"] = [i.to_dict() for i in self.recipients if isinstance(i, Recipients)]
        resp['is_ordered'] = self.is_ordered
        resp["name"] = self.name
        return resp

    def create_signature_templates(self, base_headers, base_url):
        """
        Used to create a signature request on a template
        :param base_url: string, Base URL to be pre fixed to all API
        :param base_headers: dictionary, with all the necessary tokes for transaction
        :return: tuple: json response, status code
        """
        try:
            url = base_url + "v1/files/pending/template/"

            headers = dict(base_headers)
            headers["content_type"] = "application/json"

            payload = self.to_dict()

            resp = requests.post(url=url, headers=headers, json=payload)
            return resp.json(), resp.status_code

        except Exception as e:
            return e, 400
