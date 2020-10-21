package payloads;

import org.json.JSONObject;

public class Originals {
	private String name;
	private int id;
	
	public Originals(String name, int id)
	{
		this.name = name;
		this.id = id;
	}
	
	public JSONObject toJson() 
	{
		JSONObject obj = new JSONObject();

		obj.put("name", this.name);
		obj.put("id", this.id);
		return obj;
		
	}

}
