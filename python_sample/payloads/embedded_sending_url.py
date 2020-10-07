import json
from .recipients import Recipients
from .cc import CC
import requests

type_fields = {"message": str, "type": str, "file_id": str, "cc": [CC], "recipients": [Recipients], "redirect_url": str}


class SendingUrl:
    message = ''
    cc = []
    type = ''
    recipients = []
    redirect_url = ''
    file_id = ''

    def __init__(self, *args, **kwargs):
        mandatory_fields = ["file_id"]

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
        resp["type"] = self.type
        resp["file_id"] = self.file_id
        resp["recipients"] = [i.to_dict() for i in self.recipients if isinstance(i, Recipients)]
        resp['redirect_url'] = self.redirect_url
        return json.dumps(resp)

    def to_dict(self):
        resp = dict()
        resp["message"] = self.message
        resp["cc"] = [i.to_dict() for i in self.cc if isinstance(i, CC)]
        resp["type"] = self.type
        resp["file_id"] = self.file_id
        resp["recipients"] = [i.to_dict() for i in self.recipients if isinstance(i, Recipients)]
        resp['redirect_url'] = self.redirect_url
        return resp

    def fetch_embedded_sending_url(self, base_headers, base_url):
        """
        Fetches embedded sending url for a document
        :param base_url: string, Base URL to be pre fixed to all API
        :param base_headers: dictionary, with all the necessary tokes for transaction
        :return: tuple: json response, status code
        """
        try:
            url = base_url + "v2/signing/url/"

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
