package java_sample;

import org.apache.http.client.methods.CloseableHttpResponse;

import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;

import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.entity.StringEntity;


public class SignEasyApi{
    String base_url = "https://api-ext.getsigneasy.com/";
    String api_token ;

    public SignEasyApi(String api_key){
        api_token = "Bearer " + api_key;
        System.out.println(api_token);
        }

    public CloseableHttpResponse get_all_templates() throws Exception{
    	CloseableHttpClient httpClient = HttpClients.createDefault();
    	HttpGet request = new HttpGet(base_url + "v1/library/template/");

        // add request headers
        request.addHeader("Authorization", api_token);

        CloseableHttpResponse response = httpClient.execute(request);
        return response;
       }

    public CloseableHttpResponse fetch_embedded_signing_url(String payload) throws Exception {

        HttpPost post = new HttpPost(base_url + "v2/signing/url/");
        post.addHeader("content-type", "application/json");
        post.addHeader("Authorization", api_token);

        post.setEntity(new StringEntity(payload));

        CloseableHttpClient httpClient = HttpClients.createDefault();
        CloseableHttpResponse response = httpClient.execute(post);

        return response;
    }
    /*
    public static void main(String args[])
    {
        SignEasyApi api_obj = new SignEasyApi(api_key);
        Recipients reciep_obj = new Recipients(1, "abc@gmail.com", "A");
        RequestSignature obj = new RequestSignature(1, "A", false, receip_obj);

        try{
        CloseableHttpResponse resp = obj.create_signature_templates(api_obj.base_url, api_obj.api_token);
        }
        catch(Exception e){}
    }
    */
}
