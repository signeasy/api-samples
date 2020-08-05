var unirest = require('unirest');

class UploadFile {
	constructor(name, file, rename_if_exists=false)
	{
		this.name = name;
		this.file = file;
		this.rename_if_exists = rename_if_exists;
	}

	to_json()
	{
		return {"name": this.name, "rename_if_exists": this.rename_if_exists}
	}

	upload_file = function (base_url, api_token) {
        var payload = this.to_json();
        var fs = require('fs');
        var readStream = fs.createReadStream(this.file);
        console.log(payload);
        return new Promise((resolve, reject) => {
        unirest.post(base_url + 'v1/files/original/')
        .headers({'Authorization': api_token, 'Content-Type': 'application/json'})
        .attach('file', readStream)
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

module.exports = UploadFile