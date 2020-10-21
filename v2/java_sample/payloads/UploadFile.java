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

        HttpPost post = new HttpPost(base_url + "v2/original/");
        post.addHeader("Authorization", api_token);
        
        File file = new File(this.file);
        
        MultipartEntityBuilder mpEntity = MultipartEntityBuilder.create();
        mpEntity.addTextBody("name", this.name);
        
        String rename_flag = "0";
        if (this.rename_if_exists == true) rename_flag = "1";
        
        mpEntity.addTextBody("rename_if_exists", rename_flag);
        mpEntity.addBinaryBody("file", file, ContentType.DEFAULT_BINARY, this.name);
        HttpEntity mutiPartHttpEntity = mpEntity.build();  
        
        post.setEntity(mutiPartHttpEntity);

        CloseableHttpClient httpClient = HttpClients.createDefault();
        CloseableHttpResponse response = httpClient.execute(post);

        return response;
    }
}
