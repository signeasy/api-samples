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
        var fs = require('fs');
        var readStream = fs.createReadStream(this.file);

        var rename_allowed = "0";
        if (this.rename_if_exists == true) {rename_allowed = "1";}

        return new Promise((resolve, reject) => {
        unirest.post(base_url + 'v1/files/original/')
        .headers({'Authorization': api_token, 'Content-Type': 'multipart/form-data'})
        .attach('file', readStream)
        .field("name", this.name)
        .field("rename_if_exists", rename_allowed)
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