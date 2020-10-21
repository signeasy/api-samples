package payloads;

import org.json.JSONObject;

public class EnvelopeRecipients extends Recipients{

	public EnvelopeRecipients(int role_id, String email_id, String first_name) {
		super(role_id, email_id, first_name);
	}
	
	public EnvelopeRecipients(int role_id, String email_id, String first_name, String last_name) {
		super(role_id, email_id, first_name, last_name);
	}

	public JSONObject toJson() 
	{
		JSONObject obj = new JSONObject();
		obj = super.toJson();
		obj.put("recipient_id", obj.remove("role_id"));
		return obj;
	}

}
