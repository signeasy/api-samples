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

	fetch_embedded_signing_url = function (base_url, api_token) {
        var payload = this.to_json();
        var url = base_url + `v1/files/pending/${this.id}/signing/url/`;
        console.log(payload);
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