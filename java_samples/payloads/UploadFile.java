package payloads;

import java.io.File;

import org.apache.http.HttpEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.ContentType;
import org.apache.http.entity.StringEntity;
import org.apache.http.entity.mime.MultipartEntityBuilder;
import org.apache.http.entity.mime.content.FileBody;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.json.JSONObject;

public class UploadFile {

	private String name;
	private String file;
	private boolean rename_if_exists = false;
	
	public UploadFile(String name, String file)
	{
		this.name = name;
		this.file = file;
	}
	
	public void rename_flag(boolean flag)
	{
		this.rename_if_exists  = flag;
	}
	
	public JSONObject toJson() 
	{
		JSONObject obj = new JSONObject();

		obj.put("name", this.name);
		obj.put("rename_if_exists", this.rename_if_exists);
		return obj;
	}
	
	public CloseableHttpResponse upload_file(String base_url, String api_token) throws Exception {

        HttpPost post = new HttpPost(base_url + "v1/files/original/");
        post.addHeader("Authorization", api_token);
        post.addHeader("Content-Type", "application/json");
        System.out.println(this.toJson());
        post.setEntity(new StringEntity(this.toJson().toString()));
        
        File file = new File(this.file);
        FileBody filebody = new FileBody(file, ContentType.TEXT_PLAIN);
        
        MultipartEntityBuilder mpEntity = MultipartEntityBuilder.create();
        mpEntity.addPart("file", filebody);
        HttpEntity mutiPartHttpEntity = mpEntity.build(); 
        
        post.setEntity(mutiPartHttpEntity);
        
        CloseableHttpClient httpClient = HttpClients.createDefault();
        CloseableHttpResponse response = httpClient.execute(post);
        
        org.apache.http.Header[] headers = response.getAllHeaders();
        for (org.apache.http.Header header: headers) {
            System.out.println("Key [ " + header.getName() + "], Value[ " + header.getValue() + " ]");
        }

        return response;
    }
}
