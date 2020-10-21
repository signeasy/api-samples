package payloads;

import org.json.JSONObject;

public class EnvelopeFieldsPayload extends FieldsPayload {

	private int recipient_id;
	private int original_id;

	public EnvelopeFieldsPayload(String email, String type, int page_number, double x, double y, double height,
			double width,int recipient_id,int original_id) {
		super(email, type, page_number, x, y, height, width);
		this.recipient_id = recipient_id;
		this.original_id = original_id;
	}
	
	public JSONObject toJson() 
	{
		JSONObject obj = new JSONObject();
		obj = super.toJson();
		obj.put("recipient_id", this.recipient_id);
		obj.put("original_id", this.original_id);
		
		return obj;
	}

}
