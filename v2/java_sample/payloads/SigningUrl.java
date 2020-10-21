package payloads;

import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.json.JSONObject;

public class SigningUrl {
	private int id;
	private String recipient_email;
	private String redirect_url = "";
	private boolean allow_decline = false;

	public SigningUrl(int id, String recipient_email)
	{
		this.id = id;
		this.recipient_email = recipient_email;
	}
	
	public void set_redirect_url(String val)
	{
		this.redirect_url  = val;
	}
	
	public void set_allow_decline(boolean val)
	{
		this.allow_decline   = val;
	}
	
	public JSONObject toJson() 
	{
		JSONObject obj = new JSONObject();

		obj.put("recipient_email", this.recipient_email);
		obj.put("redirect_url", this.redirect_url);
		obj.put("allow_decline", this.allow_decline);
		return obj;
	}

	public CloseableHttpResponse fetch_embedded_signing_url_for_embedded_sending(String base_url, String api_token) throws Exception 
	{
		String string = String.format("v2/rs/embedded/%d/signing/url", this.id);
        HttpPost post = new HttpPost(base_url + string);
        post.addHeader("content-type", "application/json");
        post.addHeader("Authorization", api_token);
        post.setEntity(new StringEntity(this.toJson().toString()));

        CloseableHttpClient httpClient = HttpClients.createDefault();
        CloseableHttpResponse response = httpClient.execute(post);

        return response;
    }
	
	public CloseableHttpResponse fetch_embedded_signing_url_for_envelopes(String base_url, String api_token) throws Exception 
	{
		String string = String.format("v2/rs/envelope/%d/signing/url", this.id);
        HttpPost post = new HttpPost(base_url + string);
        post.addHeader("content-type", "application/json");
        post.addHeader("Authorization", api_token);
        post.setEntity(new StringEntity(this.toJson().toString()));

        CloseableHttpClient httpClient = HttpClients.createDefault();
        CloseableHttpResponse response = httpClient.execute(post);

        return response;
    }
	
	public CloseableHttpResponse fetch_embedded_signing_url_for_templates(String base_url, String api_token) throws Exception 
	{
		String string = String.format("v2/template/rs/%d/signing/url", this.id);
        HttpPost post = new HttpPost(base_url + string);
        post.addHeader("content-type", "application/json");
        post.addHeader("Authorization", api_token);
        post.setEntity(new StringEntity(this.toJson().toString()));

        CloseableHttpClient httpClient = HttpClients.createDefault();
        CloseableHttpResponse response = httpClient.execute(post);

        return response;
    }
}
