package payloads;

import org.json.JSONObject;

public class FieldsPayload {
	private String email;
	private String type;
	private int page_number;
	private double x;
	private double y;
	private double height;
	private double width;
	private boolean required = false;
	private JSONObject additional_info = new JSONObject();

	public FieldsPayload(String email, String type, int page_number, double x, double y, double height, double width)
	{
		this.email = email;
		this.type = type;
		this.page_number = page_number;
		this.x = x;
		this.y = y;
		this.height = height;
		this.width = width;
	}
	
	public void set_required(boolean val)
	{
		this.required  = val;
	}
	
	public void set_additional_info(String key, String val)
	{
		this.additional_info.put(key, val);
	}
	
	public JSONObject toJson() 
	{
		JSONObject obj = new JSONObject();

		obj.put("email", this.email);
		obj.put("type", this.type);
		obj.put("page_number", this.page_number);
		obj.put("x", this.x);
		obj.put("y", this.y);
		obj.put("height", this.height);
		obj.put("width", this.width);
		obj.put("required", this.required);
		obj.put("additional_info", this.additional_info);
		return obj;
		
	}
}