import requests

from payloads.recipients import Recipients
from payloads.request_signature import RequestSignatures
from payloads.upload_file import UploadFile
from payloads.request_signature_with_fields import RequestSignaturesWithFields
from payloads.fields_payload import FieldsPayload
from payloads.embedded_signing_url import SigningUrl
from payloads.embedded_sending_url import SendingUrl


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


"""
Sample code

if __name__ == "__main__":
    api_obj = SignEasyApi(api_key)
    # obj = RequestSignatures(template_file_id=100,
    #                         recipients=[Recipients(first_name="xyz", email="abc@xyz.com", role_id=1)],
    #                        is_ordered=False, name="me")
    # a, b = obj.create_signature_templates(api_obj.headers, api_obj.base_url)
    # print(a, b)
    
    # obj = SendingUrl(file_id=38814455, recipients=[Recipients(first_name="xyz", email="a.b@c.com", role_id=1)])
    # a, b = obj.fetch_embedded_sending_url(api_obj.headers, api_obj.base_url)
    # obj = UploadFile(name="demo.txt",
    #                 file="/Users/demo/project/api-samples/python_sample/demo.txt")
    # a, b = obj.upload_file(api_obj.headers, api_obj.base_url)

    # obj = RequestSignaturesWithFields(original_file_id=38814455,is_ordered=False, name="me",
    #                                   recipients=[Recipients(first_name="xyz", email="a.b@c.com", role_id=1)],
    #                                   fields_payload=[FieldsPayload(email="a.b@c.com", type="text", page_number=1,
    #                                                                 x=10, y=10, width=20, height=20)])
    # a, b = obj.create_signature_request(api_obj.headers, api_obj.base_url)

    # obj = SigningUrl(id=1234, recipient_email="a.b@c.com")
    # a, b = obj.fetch_embedded_signing_url(api_obj.headers, api_obj.base_url)
    obj = SendingUrl(file_id=1245550,
                    recipients=[Recipients(first_name="xyz", email="a.b@c.com", role_id=1)])
    a, b = obj.fetch_embedded_sending_url(api_obj.headers, api_obj.base_url)
    print(a, b)
"""
