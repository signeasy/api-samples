import json
import requests

type_fields = {"id": int, "recipient_email": str, "allow_decline": bool, "redirect_url": str}


class SigningUrl:
    id = 0
    recipient_email = ''
    allow_decline = False
    redirect_url = ''

    def __init__(self, *args, **kwargs):
        mandatory_fields = ["id", "recipient_email"]
        for key, val in kwargs.items():
            setattr(self, key, val)

            if key in mandatory_fields:
                mandatory_fields.remove(key)

        if mandatory_fields:
            raise Exception("{} are missing".format(','.join(mandatory_fields)))

    def __str__(self):
        return json.dumps({"recipient_email": self.recipient_email, "allow_decline": self.allow_decline,
                           "redirect_url": self.redirect_url})

    def to_dict(self):
        return {"recipient_email": self.recipient_email, "allow_decline": self.allow_decline,
                "redirect_url": self.redirect_url}

    def __setattr__(self, name, value):
        if not isinstance(value, type_fields.get(name)):
            raise Exception("{} should be a {}".format(name, str(type_fields.get(name))))
        super().__setattr__(name, value)

    def fetch_embedded_signing_url_for_embedded_sending(self, base_headers, base_url):
        """
        Fetches embedded signing url for embedded sending RS
        :param base_url: string, Base URL to be pre fixed to all API
        :param base_headers: dictionary, with all the necessary tokes for transaction
        :return: tuple: json response, status code
        """
        try:
            url = base_url + "v2/rs/embedded/{}/signing/url".format(self.id)
            headers = dict(base_headers)
            headers["Content-Type"] = "application/json"

            payload = self.to_dict()

            resp = requests.post(url=url, headers=headers, json=payload)
            return resp.json(), resp.status_code

        except Exception as e:
            return e, 400

    def fetch_embedded_signing_url_for_envelopes(self, base_headers, base_url):
        """
        Fetches embedded signing url for envelopes
        :param base_url: string, Base URL to be pre fixed to all API
        :param base_headers: dictionary, with all the necessary tokes for transaction
        :return: tuple: json response, status code
        """
        try:
            url = base_url + "v2/rs/envelope/{}/signing/url".format(self.id)
            headers = dict(base_headers)
            headers["Content-Type"] = "application/json"

            payload = self.to_dict()

            resp = requests.post(url=url, headers=headers, json=payload)
            return resp.json(), resp.status_code

        except Exception as e:
            return e, 400

    def fetch_embedded_signing_url_for_templates(self, base_headers, base_url):
        """
        Fetches embedded signing url for templates
        :param base_url: string, Base URL to be pre fixed to all API
        :param base_headers: dictionary, with all the necessary tokes for transaction
        :return: tuple: json response, status code
        """
        try:
            url = base_url + "v2/template/rs/{}/signing/url".format(self.id)
            headers = dict(base_headers)
            headers["Content-Type"] = "application/json"

            payload = self.to_dict()

            resp = requests.post(url=url, headers=headers, json=payload)
            return resp.json(), resp.status_code

        except Exception as e:
            return e, 400
