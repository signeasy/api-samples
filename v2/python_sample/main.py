import requests
from payloads.upload_file import UploadFile
from payloads.embedded_sending_url import SendingUrl
from payloads.recipients import Recipients, EnvelopeRecipients
from payloads.request_signature_template import RequestSignatures
from payloads.request_signature_with_fields import RequestSignaturesWithFields
from payloads.fields_payload import FieldsPayload, EnvelopesFieldsPayload
from payloads.originals import Originals
from payloads.embedded_signing_url import SigningUrl


class SignEasyApi:
    base_url = "https://api.signeasy.com/"

    def __init__(self, api_token):
        self.headers = {"Authorization": "Bearer {}".format(api_token)}

    def get_all_templates(self):
        """
        Used to fecth all templates in account
        :return: response: dict status_code: int
        """
        url = self.base_url + "v2/template/"

        resp = requests.get(url=url, headers=self.headers)
        return resp.json(), resp.status_code

"""
Sample code

if __name__ == "__main__":
    # api_obj = SignEasyApi(api_key)

    # obj = UploadFile(name="demo_sample.txt",
    #                file="/Users/user/project/api-samples/v1/python_sample/demo.txt")
    # a, b = obj.upload_file(api_obj.headers, api_obj.base_url)

    # obj = SendingUrl(file_id="41038497", recipients=[Recipients(first_name="xyz", email="a.b@c.com", role_id=1)])
    # a, b = obj.fetch_embedded_sending_url(api_obj.headers, api_obj.base_url)

    # obj = RequestSignatures(template_file_id=4194181, recipients=[Recipients(first_name="xyz", email="abc@xyz.com", role_id=1)],
    #                       is_ordered=False, name="me", embedded_signing=True)
    # a, b = obj.create_signature_templates(api_obj.headers, api_obj.base_url)

    # obj = RequestSignaturesWithFields(originals=[Originals(id=41038497, name="demofields")], is_ordered=False, name="demo fields",
    #                                  recipients=[EnvelopeRecipients(first_name="xyz", email="a.b@c.com", recipient_id=1)],
    #                                  fields_payload=[EnvelopesFieldsPayload(email="a.b@c.com", type="text", page_number=1,
    #                                                                x=10, y=10, width=20, height=20, recipient_id=1, original_id=1)])
    # a, b = obj.create_signature_request(api_obj.headers, api_obj.base_url)
    # obj = SigningUrl(id=1462202, recipient_email="abc@xyz.com")
    # a, b = obj.fetch_embedded_signing_url_for_embedded_sending(api_obj.headers, api_obj.base_url)
    # print(a, b)
    # a, b = obj.fetch_embedded_signing_url_for_envelopes(api_obj.headers, api_obj.base_url)
    # print(a, b)
    # a, b = obj.fetch_embedded_signing_url_for_templates(api_obj.headers, api_obj.base_url)
    # print(a, b)"""
