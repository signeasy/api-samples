package payloads;

import java.util.ArrayList;

import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.json.JSONObject;

public class RequestSignatureWithFields {
	
	private int original_file_id;
	private boolean is_ordered;
	private String name;
	private ArrayList<Recipients> recipients = new ArrayList<Recipients>();
	private String message = "";
	private ArrayList<CC> cc = new ArrayList<CC>();
	private boolean embedded_signing = false;
	private ArrayList<MergeFields> merge_fields = new ArrayList<MergeFields>();
	private ArrayList<FieldsPayload> fields_payload = new ArrayList<FieldsPayload>();

	public RequestSignatureWithFields(int original_file_id, Recipients recipients, boolean is_ordered, String name, 
			FieldsPayload fields_payload)
	{
		this.original_file_id = original_file_id;
		this.recipients.add(recipients);
		this.is_ordered = is_ordered;
		this.name = name;
		this.fields_payload.add(fields_payload);
		
	}
	
	public void set_message(String msg) 
	{
		this.message = msg;
	}
	
	public void add_cc(CC obj) 
	{
		this.cc.add(obj);
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
		
		for (int i = 0; i < this.fields_payload.size(); i++)  
		{
            array.add(this.fields_payload.get(i).toJson());         
		} 
		obj.put("fields_payload", array);
		array.clear();
		
		obj.put("original_file_id", this.original_file_id);
		obj.put("is_ordered", this.is_ordered);
		obj.put("name", this.name);
		obj.put("message", this.message);
		
		
		obj.put("embedded_signing", this.embedded_signing);
		
		return obj;
		
	}
	
	public CloseableHttpResponse create_signature_requests(String base_url, String api_token) throws Exception {

        HttpPost post = new HttpPost(base_url + "v1/files/pending/fields/");
        post.addHeader("content-type", "application/json");
        post.addHeader("Authorization", api_token);
        post.setEntity(new StringEntity(this.toJson().toString()));

        CloseableHttpClient httpClient = HttpClients.createDefault();
        CloseableHttpResponse response = httpClient.execute(post);

        return response;
    }
	/*
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		RequestSignatureWithFields obj = new RequestSignatureWithFields(1, new Recipients(1, "a", "a"), false, "a", 
				new FieldsPayload("a", "A", 1, 2, 3, 4, 5));
		System.out.println(obj.toJson());
	}*/
}
