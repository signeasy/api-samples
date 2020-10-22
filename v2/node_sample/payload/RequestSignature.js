const Recipients = require('./Recipients');
const CC = require('./CC');
const MergeFields = require('./MergeFields');
var unirest = require('unirest');

class RequestSignature
{
    message = ''
    cc = []
    file_password = ''
    embedded_signing = false
    merge_fields = []
    template_file_id = 0
    recipients = []
    is_ordered = false
    name = ''

    constructor(template_file_id, recipients, is_ordered, name, message='', cc=null, file_password='',
                embedded_signing=false, merge_fields=null)
  {
    this.template_file_id = template_file_id;
    this.add_recipients(recipients);
    this.is_ordered = is_ordered;
    this.name = name;
    this.message = message;

    if (cc != null)
    {
        this.add_cc(cc)
    }
    this.file_password = file_password;
    this.embedded_signing = embedded_signing;

    if (merge_fields != null)
    {
        this.add_merge_fields(merge_fields);
    }
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

  add_merge_fields(merge_fields)
  {
    if (!(merge_fields instanceof MergeFields))
    {
        throw new Error("Invalid type of merge_fields");
    }
    this.merge_fields.push(merge_fields);
  }

  to_json()
  {
        return  {"template_file_id": this.template_file_id, "is_ordered": this.is_ordered, "name": this.name,
                 "recipients": this.recipients, "cc": this.cc, "message": this.message, "merge_fields": this.merge_fields,
                 "file_password": this.file_password, "embedded_signing": this.embedded_signing}
  }

  create_signature_templates = function (base_url, api_token) {
        var payload = this.to_json();
        return new Promise((resolve, reject) => {
        unirest.post(base_url + `v2/template/${this.template_file_id}/rs`)
        .headers({'Authorization': api_token, 'content-type': "application/json"})
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

module.exports = RequestSignature
/*
try{
obj = new RequestSignature(0, "a", false, "c");
console.log(obj.to_json());
}
catch (e){
console.log(e.message);
}*/