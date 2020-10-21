package java_api_samples;

import org.apache.http.client.methods.CloseableHttpResponse;

import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;

import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

import payloads.FieldsPayload;
import payloads.Recipients;
import payloads.RequestSignature;
import payloads.RequestSignatureWithFields;
import payloads.SendingUrl;
import payloads.SigningUrl;
import payloads.UploadFile;

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

    /*
    Sample code

    public static void main(String args[])
    {//1245550
        SignEasyApi api_obj = new SignEasyApi(api_key);
        //Recipients reciep_obj = new Recipients(1, "abc@gmail.com", "A");
        //RequestSignature obj = new RequestSignature(1, "A", false, reciep_obj);

        //RequestSignatureWithFields obj = new RequestSignatureWithFields(38814455, new Recipients(1, "abc@gmail.com", "abc@gmail.com"),
        //	                                       false, "a", new FieldsPayload("abc@gmail.com", "text", 1, 10,10, 20,20));
        //UploadFile obj = new UploadFile("2019ht13102.pdf", "/Users/demo/project/api-samples/python_sample/2019ht13102.pdf");
        //SigningUrl obj = new SigningUrl(1245550, "abc.cde@gmail.com");
        SendingUrl obj = new SendingUrl("1245550", new Recipients(1, "a.b@c.com", "A"));
        try{
        CloseableHttpResponse resp = obj.fetch_embedded_sending_url(api_obj.base_url, api_obj.api_token);
        System.out.println(resp.getStatusLine().getStatusCode());
        System.out.println(EntityUtils.toString((resp.getEntity())));
        }
        catch(Exception e){}
    }*/
    
}

