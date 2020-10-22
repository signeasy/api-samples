var unirest = require('unirest');

class SigningUrl {
	constructor(id, recipient_email, allow_decline=false, redirect_url='')
	{
		this.id = id;
		this.recipient_email = recipient_email;
		this.allow_decline = allow_decline;
		this.redirect_url = redirect_url;
	}

	to_json()
	{
		return {"recipient_email": this.recipient_email, "allow_decline": this.allow_decline,
		"redirect_url": this.redirect_url}
	}

	fetch_embedded_signing_url_for_embedded_sending = function (base_url, api_token) {
        var payload = this.to_json();
        var url = base_url + `v2/rs/embedded/${this.id}/signing/url`;
        return new Promise((resolve, reject) => {
        unirest.post(url)
        .headers({'Authorization': api_token, 'Content-Type': 'application/json'})
        .send(payload)
        .end(function (response) {
        if (response.error) {
        return reject(response.body)
        }
        return resolve(response.body);
        });
    })
    }

    fetch_embedded_signing_url_for_envelopes = function (base_url, api_token) {
        var payload = this.to_json();
        var url = base_url + `v2/rs/envelope/${this.id}/signing/url`;
        return new Promise((resolve, reject) => {
        unirest.post(url)
        .headers({'Authorization': api_token, 'Content-Type': 'application/json'})
        .send(payload)
        .end(function (response) {
        if (response.error) {
        return reject(response.body)
        }
        return resolve(response.body);
        });
    })
    }

    fetch_embedded_signing_url_for_templates = function (base_url, api_token) {
        var payload = this.to_json();
        var url = base_url + `v2/template/rs/${this.id}/signing/url`;
        return new Promise((resolve, reject) => {
        unirest.post(url)
        .headers({'Authorization': api_token, 'Content-Type': 'application/json'})
        .send(payload)
        .end(function (response) {
        if (response.error) {
        return reject(response.body)
        }
        return resolve(response.body);
        });
    })
    }
}

module.exports = SigningUrl