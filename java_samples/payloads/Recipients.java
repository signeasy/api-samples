package payloads;

import org.json.JSONObject;

public class Recipients {
	private String email;
	private int role_id;
	private String first_name;
	private String last_name = "";

	public recipients(int role_id, String email_id, String first_name, String last_name) 
	{
		this.first_name = first_name;
		this.role_id = role_id;
		this.email = email_id;
		this.last_name = last_name;
	}
	
	public recipients(int role_id, String email_id, String first_name) 
	{
		this.first_name = first_name;
		this.role_id = role_id;
		this.email = email_id;
	}
	
	
	public JSONObject toJson() 
	{
		JSONObject obj = new JSONObject();

		obj.put("first_name", this.first_name);
		obj.put("last_name", this.last_name);
		obj.put("email", this.email);
		obj.put("role_id", this.role_id);
		return obj;
		
	}
}
