const FieldsPayload = require('./FieldsPayload');

class EnvelopeFieldsPayload extends FieldsPayload {
	constructor(email, type, page_number, x, y, height, width, recipient_id, original_id,
	required=false, additional_info={})
	{
	    super(email, type, page_number, x, y, height, width, required=false, additional_info={})
		this.recipient_id = recipient_id;
		this.original_id = original_id;
	}

	to_json()
	{
	    var obj = super.to_json();
		obj["recipient_id"] = this.recipient_id;
		obj["original_id"] = this.original_id;
		return obj
	}
}

module.exports = EnvelopeFieldsPayload