var unirest = require('unirest');

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

   create_signature_templates = function (payload) {
        return new Promise((resolve, reject) => {
        unirest.post(this.base_url + 'v1/files/pending/template/')
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
