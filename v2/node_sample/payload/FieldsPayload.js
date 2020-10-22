class FieldsPayload {
	constructor(email, type, page_number, x, y, height, width, required=false, additional_info={})
	{
		this.email = email;
		this.type = type;
		this.page_number = page_number;
		this.x = x;
		this.y = y;
		this.height = height;
		this.width = width;
		this.required = required;
		this.additional_info = additional_info;
	}

	to_json()
	{
		return {"email": this.email, "type": this.type, "page_number": this.page_number, "x": this.x, "y": this.y,
		"height": this.height, "width": this.width, "required": this.required,"additional_info": this.additional_info}
	}
}

module.exports = FieldsPayload