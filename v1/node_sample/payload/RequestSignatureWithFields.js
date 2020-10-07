const Recipients = require('./Recipients');
const CC = require('./CC');
const MergeFields = require('./MergeFields');
const FieldsPayload = require('./FieldsPayload');
var unirest = require('unirest');

class RequestSignatureWithFields {
    recipients = []
    fields_payload = []
    cc = []
    merge_fields = []

	constructor(original_file_id, recipients, is_ordered, name, fields_payload, message='', cc=null,
	embedded_signing=false, merge_fields=null)
	{
    this.original_file_id = original_file_id;
    this.add_recipients(recipients);
    this.is_ordered = is_ordered;
    this.name = name;
    this.add_fields_payload(fields_payload);
    this.message = message;

    if (cc != null)
    {
        this.add_cc(cc)
    }
    this.embedded_signing = embedded_signing;

    if (merge_fields != null)
    {
        this.add_merge_fields(merge_fields);
    }
   }

    add_fields_payload(fields_payload)
    {
    if (!(fields_payload instanceof FieldsPayload))
    {
        throw new Error("Invalid type of Fields payload");
    }
    this.fields_payload.push(fields_payload);
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

    to_json(){
    return {"original_file_id": this.original_file_id, "recipients": this.recipients, "is_ordered": this.is_ordered,
    "name": this.name, "fields_payload": this.fields_payload, "message": this.message, "cc": this.cc,
    "embedded_signing": this.embedded_signing, merge_fields: this.merge_fields}
     }

     create_signature_requests = function (base_url, api_token) {
        var payload = this.to_json();
        console.log(payload);
        return new Promise((resolve, reject) => {
        unirest.post(base_url + 'v1/files/pending/fields/')
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

module.exports = RequestSignatureWithFields