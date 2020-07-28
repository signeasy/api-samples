package payloads;

import org.json.JSONObject;

public class merge_fields {
	private String label;
	private String value;
	private int font_size = 0;

	public merge_fields(String label, String value, int font_size) 
	{
		this.label = label;
		this.value = value;
		this.font_size  = font_size;
	}
	
	public merge_fields(String label, String value)
	{
		this.label = label;
		this.value = value;
	}
	
	
	public JSONObject toJson() 
	{
		JSONObject obj = new JSONObject();

		obj.put("label", this.label);
		obj.put("value", this.value);
		obj.put("font_size", this.font_size);
		return obj;
		
	}

}
