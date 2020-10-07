var unirest = require('unirest');
const Recipients = require('./Recipients');
const CC = require('./CC');

class SendingUrl {
    recipients = []
    cc = []

	constructor(file_id, recipients, message='', redirect_url='', cc=null, type='')
	{
		this.file_id = file_id;
		this.add_recipients(recipients);
        this.message = message;

        if (cc != null)
        {
            this.add_cc(cc)
        }
        this.type = type;
        this.redirect_url = redirect_url;

      }

      add_recipients(recipients)
      {
        if (!(recipients instanceof Recipients))
        {
            throw new Error("Invalid type of recipients");
        }
        this.recipients.push(recipients);
      }

      add_cc(cc)
      {
        if (!(cc instanceof CC))
        {
            throw new Error("Invalid type of cc");
        }
        this.cc.push(cc);
      }

      to_json()
      {
            return  {"file_id": this.file_id, "type": this.type, "message": this.message,
                     "recipients": this.recipients, "cc": this.cc, "redirect_url": this.redirect_url}
      }

      fetch_embedded_sending_url = function (base_url, api_token) {
        var payload = this.to_json();
        var url = base_url + "v2/signing/url/";
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

module.exports = SendingUrl