import json
import requests

type_fields = {"name": str, "file": str, "rename_if_exists": bool}


class UploadFile:
    name = ""
    file = ""
    rename_if_exists = False

    def __init__(self, *args, **kwargs):
        mandatory_fields = ["name", "file"]

        for key, val in kwargs.items():
            setattr(self, key, val)
            if key in mandatory_fields:
                mandatory_fields.remove(key)

        if mandatory_fields:
            raise Exception("{} are missing".format(','.join(mandatory_fields)))

    def __setattr__(self, key, value):
        if not isinstance(value, type_fields.get(key)):
            raise Exception("{} should be a {}".format(key, type_fields.get(key)))
        super().__setattr__(key, value)

    def upload_file(self, base_headers, base_url):
        """
        Used to create a signature request on a template
        :param base_url: string, Base URL to be pre fixed to all API
        :param base_headers: dictionary, with all the necessary tokes for transaction
        :return: tuple: json response, status code
        """
        try:
            url = base_url + "v1/files/original/"

            headers = dict(base_headers)
            headers["Content-Type"] = "multipart/form-data"

            payload = self.to_dict()

            with open(payload['file'], 'rb') as file:
                del payload['file']
                resp = requests.post(url=url, headers=headers, json=payload, files={"file": file})
            return resp.json(), resp.status_code

        except Exception as e:
            return e, 400

    def __str__(self):
        resp = dict()
        resp["name"] = self.name
        resp["file"] = self.file
        resp["rename_if_exists"] = self.rename_if_exists
        return json.dumps(resp)

    def to_dict(self):
        resp = dict()
        resp["name"] = self.name
        resp["file"] = self.file
        resp["rename_if_exists"] = self.rename_if_exists
        return resp
