package payloads;

import java.util.ArrayList;

import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.json.JSONObject;

public class RequestSignatureWithFields {
	
	private ArrayList<Originals> original = new ArrayList<Originals>();
	private boolean is_ordered;
	private String name;
	private ArrayList<EnvelopeRecipients> recipients = new ArrayList<EnvelopeRecipients>();
	private String message = "";
	private ArrayList<CC> cc = new ArrayList<CC>();
	private boolean embedded_signing = false;
	private ArrayList<MergeFields> merge_fields = new ArrayList<MergeFields>();
	private ArrayList<EnvelopeFieldsPayload> fields_payload = new ArrayList<EnvelopeFieldsPayload>();

	public RequestSignatureWithFields(Originals original, EnvelopeRecipients recipients, boolean is_ordered, String name, 
			EnvelopeFieldsPayload fields_payload)
	{
		this.original.add(original);
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
	
	public void add_recipients(EnvelopeRecipients obj) 
	{
		this.recipients.add(obj);
	}
	
	public void add_originals(Originals obj) 
	{
		this.original.add(obj);
	}
	
	public void add_fields_payload(EnvelopeFieldsPayload obj) 
	{
		this.fields_payload.add(obj);
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
		
		for (int i = 0; i < this.original.size(); i++)  
		{
            array.add(this.original.get(i).toJson());         
		} 
		obj.put("originals", array);
		array.clear();
		
		obj.put("is_ordered", this.is_ordered);
		obj.put("name", this.name);
		obj.put("message", this.message);
		
		
		obj.put("embedded_signing", this.embedded_signing);
		
		return obj;
		
	}
	
	public CloseableHttpResponse create_signature_requests(String base_url, String api_token) throws Exception {

        HttpPost post = new HttpPost(base_url + "v2/rs/envelope");
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
