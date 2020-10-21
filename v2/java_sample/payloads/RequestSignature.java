package payloads;
import java.util.ArrayList;

import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.json.JSONObject;

public class RequestSignature {
	
	private int template_file_id;
	private boolean is_ordered;
	private String name;
	private ArrayList<Recipients> recipients = new ArrayList<Recipients>();
	private String message = "";
	private ArrayList<CC> cc = new ArrayList<CC>();
	private String file_password = "";
	private boolean embedded_signing = false;
	private ArrayList<MergeFields> merge_fields = new ArrayList<MergeFields>();

	public RequestSignature(int template_file_id, String name, boolean is_ordered, Recipients recip)
	{
		this.template_file_id = template_file_id;
		this.is_ordered = is_ordered;
		this.name  = name;
		this.recipients.add(recip);
	}
	
	public void set_message(String msg) 
	{
		this.message = msg;
	}
	
	public void add_cc(CC obj) 
	{
		this.cc.add(obj);
	}
	
	public void set_file_password(String msg) 
	{
		this.file_password = msg;
	}
	
	public void set_embedded_signing(boolean msg) 
	{
		this.embedded_signing = msg;
	}
	
	public void add_merge_field(MergeFields obj) 
	{
		this.merge_fields.add(obj);
	}
	
	public void add_recipients(Recipients obj) 
	{
		this.recipients.add(obj);
	}
	
	public JSONObject toJson() 
	{
		JSONObject obj = new JSONObject();

		ArrayList<JSONObject> array = new ArrayList<JSONObject>();
		
		for (int i = 0; i < this.recipients.size(); i++)  
		{
            array.add(this.recipients.get(i).toJson());         
		} 
		obj.put("recipients", array);
		array.clear();
		
		for (int i = 0; i < this.cc.size(); i++)  
		{
            array.add(this.cc.get(i).toJson());         
		} 
		obj.put("cc", array);
		array.clear();
		
		for (int i = 0; i < this.merge_fields.size(); i++)  
		{
            array.add(this.merge_fields.get(i).toJson());         
		} 
		obj.put("merge_fields", array);
		array.clear();
		
		obj.put("template_file_id", this.template_file_id);
		obj.put("is_ordered", this.is_ordered);
		obj.put("name", this.name);
		obj.put("message", this.message);
		
		
		obj.put("file_password", this.file_password);
		obj.put("embedded_signing", this.embedded_signing);
		
		return obj;
		
	}
	
	public CloseableHttpResponse create_signature_templates(String base_url, String api_token) throws Exception {

		String string = String.format("v2/template/%d/rs", this.template_file_id);
		HttpPost post = new HttpPost(base_url + string);
        post.addHeader("content-type", "application/json");
        post.addHeader("Authorization", api_token);
        post.setEntity(new StringEntity(this.toJson().toString()));

        CloseableHttpClient httpClient = HttpClients.createDefault();
        CloseableHttpResponse response = httpClient.execute(post);

        return response;
    }


}
