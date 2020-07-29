var unirest = require('unirest');
const Recipients = require('./payload/Recipients');
const CC = require('./payload/CC');
const MergeFields = require('./payload/MergeFields');
const RequestSignature = require('./payload/RequestSignature');

class SignEasyApi
{
  base_url = "https://api-ext.getsigneasy.com/";

  constructor(api_key)
  {
    this.api_token = "Bearer " + api_key;
  }

   get_all_templates = function () {
       return new Promise((resolve, reject) => {
            unirest.get(this.base_url + 'v1/library/template/')
            .headers({'Authorization': this.api_token})
            .end(function (response) {
            if (response.error) {
            return reject(response.error)
            }
            return resolve(response.body);
            });
    })
    }

   fetch_embedded_signing_url = function (payload) {
        return new Promise((resolve, reject) => {
        unirest.post(this.base_url + 'v2/signing/url/')
        .headers({'Authorization': this.api_token, 'content-type': "application/json"})
        .send(payload)
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
api_obj = new SignEasyApi("api_key");
rs_obj = new RequestSignature(100, new Recipients(1, "abc@xyz.com", "R"), false, "R");
rs_obj.create_signature_templates(api_obj.base_url, api_obj.api_token).then((body) =>
console.log("success", body)).catch((error) => console.log("error", error))
*/