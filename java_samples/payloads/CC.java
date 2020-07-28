package payloads;

import org.json.JSONObject;

public class CC {
	private String email;
	
	public cc(String email) 
	{
		this.email = email;
	}
	
	
	public JSONObject toJson() 
	{
		JSONObject obj = new JSONObject();

		obj.put("email", this.email);
		return obj;
		
	}
	
}
