import requests


class SignEasyApi:
    base_url = "https://api-ext.getsigneasy.com/"

    def __init__(self, api_token):
        self.headers = {"Authorization": "Bearer {}".format(api_token)}

    def get_all_templates(self):
        """
        Used to fecth all templates in account
        :return: response: dict status_code: int
        """
        url = self.base_url + "v1/library/template/"

        resp = requests.get(url=url, headers=self.headers)
        return resp.json(), resp.status_code

    def create_signature_templates(self, data):
        """
        Used to create a signature request on a template
        :param data: dictionary, with all the necessary fields for transaction
        :return: tuple: json response, status code
        """
        try:
            url = self.base_url + "v1/files/pending/template/"

            mandatory_fields = ["template_file_id", "recipients", "is_ordered", "name"]
            optional_fields = ["message", "cc", "file_password", "embedded_signing", "merge_fields"]

            if not all(i in data for i in mandatory_fields):
                raise Exception("Mandatory fields are missing")

            payload = {i: data[i] for i in mandatory_fields+optional_fields if i in data}

            headers = dict(self.headers)
            headers["content_type"] = "application/json"

            resp = requests.post(url=url, headers=headers, json=payload)
            return resp.json(), resp.status_code

        except Exception as e:
            return e, 400

    def fetch_embedded_signing_url(self, data):
        """
        Used to send an url for embedded signing
        :param data: dictionary, with all the necessary fields for transaction
        :return: tuple: json response, status code
        """
        try:
            url = self.base_url + "v2/signing/url/"

            mandatory_fields = ["file_id", "recipients"]
            optional_fields = ["message", "cc", "type", "redirect_url"]

            if not all(i in data for i in mandatory_fields):
                raise Exception("Mandatory fields are missing")

            payload = {i: data[i] for i in mandatory_fields+optional_fields if i in data}

            headers = dict(self.headers)
            headers["content_type"] = "application/json"

            resp = requests.post(url=url, headers=headers, json=payload)
            print(resp.json())
            return resp.json(), resp.status_code

        except Exception as e:
            return e, 400
