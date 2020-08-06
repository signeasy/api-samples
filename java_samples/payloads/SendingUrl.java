package payloads;

import java.util.ArrayList;

import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.json.JSONObject;

public class SendingUrl {
	private String type = "";
	private ArrayList<Recipients> recipients = new ArrayList<Recipients>();
	private String message = "";
	private ArrayList<CC> cc = new ArrayList<CC>();
	private String file_id;
	private String redirect_url = "";

	public SendingUrl(String file_id, Recipients recip)
	{
		this.file_id = file_id;
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
	
	public void set_type(String msg) 
	{
		this.type = msg;
	}
	
	public void set_redirect_url(String msg) 
	{
		this.redirect_url = msg;
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
		
		
		obj.put("file_id", this.file_id);
		obj.put("type", this.type);
		obj.put("message", this.message);
		
		
		obj.put("redirect_url", this.redirect_url);
		
		return obj;
		
	}
	
	public CloseableHttpResponse fetch_embedded_sending_url(String base_url, String api_token) throws Exception {

        HttpPost post = new HttpPost(base_url + "v2/signing/url/");
        post.addHeader("content-type", "application/json");
        post.addHeader("Authorization", api_token);
        post.setEntity(new StringEntity(this.toJson().toString()));

        CloseableHttpClient httpClient = HttpClients.createDefault();
        CloseableHttpResponse response = httpClient.execute(post);

        return response;
    }
	
}
