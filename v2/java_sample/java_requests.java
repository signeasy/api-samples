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
import payloads.Originals;
import payloads.EnvelopeRecipients;
import payloads.EnvelopeFieldsPayload;

import org.apache.http.entity.StringEntity;


public class SignEasyApi{
    String base_url = "https://api.signeasy.com/";
    String api_token ;

    public SignEasyApi(String api_key){
        api_token = "Bearer " + api_key;
        System.out.println(api_token);
        }

    public CloseableHttpResponse get_all_templates() throws Exception{
    	CloseableHttpClient httpClient = HttpClients.createDefault();
    	HttpGet request = new HttpGet(base_url + "v2/template/");

        // add request headers
        request.addHeader("Authorization", api_token);

        CloseableHttpResponse response = httpClient.execute(request);
        return response;
       }

/*
Samples

    public static void main(String args[])
    {
        SignEasyApi api_obj = new SignEasyApi(api_key);
        // UploadFile obj = new UploadFile("2019ht13102.pdf", "/Users/demo/project/api-samples/v1/python_sample/2019ht13102.pdf");
        // SendingUrl obj = new SendingUrl("41038497", new Recipients(1, "a@b.com", "XYZ"));
        // RequestSignature obj = new RequestSignature(4194181, "me", false, new Recipients(1, "a@b.com", "XYZ"));
        // RequestSignatureWithFields obj = new RequestSignatureWithFields()
        //RequestSignatureWithFields obj = new RequestSignatureWithFields(new Originals("demofields", 41038497), new EnvelopeRecipients(1, "a@b.com", "XYZ"),
        //		false, "sample", new EnvelopeFieldsPayload("a@b.com", "text", 1, 10, 10, 20, 20, 1, 1));
        SigningUrl obj = new SigningUrl(1462202, "abc@xyz.com");
        try{
            // CloseableHttpResponse resp = api_obj.get_all_templates();
        	// CloseableHttpResponse resp = obj.upload_file(api_obj.base_url, api_obj.api_token);
        	// CloseableHttpResponse resp = obj.fetch_embedded_sending_url(api_obj.base_url, api_obj.api_token);
        	// CloseableHttpResponse resp = obj.create_signature_templates(api_obj.base_url, api_obj.api_token);
        	// CloseableHttpResponse resp = obj.create_signature_requests(api_obj.base_url, api_obj.api_token);
        	// CloseableHttpResponse resp = obj.fetch_embedded_signing_url_for_embedded_sending(api_obj.base_url, api_obj.api_token);
        	// CloseableHttpResponse resp = obj.fetch_embedded_signing_url_for_envelopes(api_obj.base_url, api_obj.api_token);
        	// CloseableHttpResponse resp = obj.fetch_embedded_signing_url_for_templates(api_obj.base_url, api_obj.api_token);
        	// System.out.println(resp.getStatusLine().getStatusCode());
            // System.out.println(EntityUtils.toString((resp.getEntity())));
            }
            catch(Exception e){}
        }*/
    
}

