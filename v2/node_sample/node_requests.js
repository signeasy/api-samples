var unirest = require('unirest');

const EnvelopeRecipients = require('./payload/EnvelopeRecipients');
const CC = require('./payload/CC');
const MergeFields = require('./payload/MergeFields');
const RequestSignature = require('./payload/RequestSignature');
const RequestSignatureWithFields = require('./payload/RequestSignatureWithFields');
const EnvelopeFieldsPayload = require('./payload/EnvelopeFieldsPayload');
const UploadFile = require('./payload/UploadFile');
const SigningUrl = require('./payload/SigningUrl');
const SendingUrl = require('./payload/SendingUrl');
const Originals = require('./payload/Originals');

class SignEasyApi
{
  base_url = "https://api.signeasy.com/";

  constructor(api_key)
  {
    this.api_token = "Bearer " + api_key;
  }

   get_all_templates = function () {
       return new Promise((resolve, reject) => {
            unirest.get(this.base_url + 'v2/template/')
            .headers({'Authorization': this.api_token})
            .end(function (response) {
            if (response.error) {
            return reject(response.error)
            }
            return resolve(response.body);
            });
    })
    }

}

/*
Sample code

api_obj = new SignEasyApi("api_key");

//api_obj.get_all_templates(api_obj.base_url, api_obj.api_token).then((body) =>
//console.log("success", body)).catch((error) => console.log("error", error))

//rs_obj = new UploadFile("demo.pdf", "/Users/demo/Downloads/hall_ticket.pdf");
//rs_obj.upload_file(api_obj.base_url, api_obj.api_token).then((body) =>
//console.log("success", body)).catch((error) => console.log("error", error));

//rs_obj = new SendingUrl(41038497, new Recipients(1, "abc@xyz.com", "R"));
//rs_obj.fetch_embedded_sending_url(api_obj.base_url, api_obj.api_token).then((body) =>
//console.log("success", body)).catch((error) => console.log("error", error));

//rs_obj = new RequestSignature(4194181, new Recipients(1, "abc@xyz.com", "R"), false, "R");
//rs_obj.create_signature_templates(api_obj.base_url, api_obj.api_token).then((body) =>
//console.log("success", body)).catch((error) => console.log("error", error))

//rs_obj = new RequestSignatureWithFields(new Originals(41038497, "demofields"),
//                                        new EnvelopeRecipients(1, "a.b@c.com", "a.b@c.com"),
//                                        false, "a", new EnvelopeFieldsPayload("a.b@c.com", "text", 1, 10,10, 20,20, 1, 1));
//rs_obj.create_signature_requests(api_obj.base_url, api_obj.api_token).then((body) =>
//console.log("success", body)).catch((error) => console.log("error", error));

rs_obj = new SigningUrl(1462202, "abc@xyz.com");
rs_obj.fetch_embedded_signing_url_for_embedded_sending(api_obj.base_url, api_obj.api_token).then((body) =>
console.log("success", body)).catch((error) => console.log("error", error));

rs_obj = new SigningUrl(1462202, "abc@xyz.com");
rs_obj.fetch_embedded_signing_url_for_envelopes(api_obj.base_url, api_obj.api_token).then((body) =>
console.log("success", body)).catch((error) => console.log("error", error));

rs_obj = new SigningUrl(1462202, "abc@xyz.com");
rs_obj.fetch_embedded_signing_url_for_templates(api_obj.base_url, api_obj.api_token).then((body) =>
console.log("success", body)).catch((error) => console.log("error", error));
*/