Code samples to help integrating the Signeasy API

# Python Setup
For Python, First we need to setup virtual environment with all the dependent libraries which are mentioned in 
`python_requirements.txt` . These libraries can be installed using the following command:

``pip install -r python_requirements.txt``

In `main.py` the base class `SignEasyApi` has to be instantiated first with the user api key provided on our
 [website](https://api-demo.getsigneasy.com). This object will serve as the base object and it is required 
while using any of our services.
```
api_obj = SignEasyApi(api key)
```

# Java Setup
For Java, First we need to setup all the dependent libraries which are mentioned in 
`java_requirements.xml` . These libraries can be installed by adding this code to build configuration.

In `java_requests.java` the base class `SignEasyApi` has to be instantiated first with the user api key provided on our
 [website](https://api-demo.getsigneasy.com). This object will serve as the base object and it is required 
while using any of our services.
```
SignEasyApi api_obj = new SignEasyApi(api_key)
```

# NodeJS Setup
For Node, First we need to setup all the dependent libraries which are mentioned in 
`node_requirements.json` . These libraries can be installed by adding this code to package.json and executing the command:

``npm install``

In `node_requests.js` the base class `SignEasyApi` has to be instantiated first with the user api key provided on our
 [website](https://api-demo.getsigneasy.com). This object will serve as the base object and it is required 
while using any of our services.
```
api_obj = new SignEasyApi(api_key)
```

---
**Note:**

From now on we will be using the above mentioned object as api_obj in all the examples.

---

## 1- Get all templates
### Python
The source code is available in `python_sample/main.py`.

Sample Example in Python - 
```
api_obj.get_all_templates()    # This should return json, status code
```

### Java
The source code is available in `java_samples/java_requests.java`.

Sample Example in Java - 
```
try{
CloseableHttpResponse resp = api_obj.get_all_templates();}
catch(Exception e){}
```

### Node 
The code is available in `node_sample/node_requests.js`.

Sample Example in Node -
```
api_obj.get_all_templates().then((body) =>console.log("success", body)).catch((error) => console.log("error", error))
```

##2- Create Signature request with template
### Python
The source code is available in `python_sample/payloads/request_signature.py`.

Sample Example in Python - 
```
obj = RequestSignatures(template_file_id=100, recipients=[Recipients(first_name="xyz", email="abc@xyz.com", role_id=1)],
                        is_ordered=False, name="me")
resp, code = obj.create_signature_templates(api_obj.headers, api_obj.base_url)    # This should return json, status code
```

### Java
The source code is available in `java_samples/payloads/RequestSignature.java`.

Sample Example in Java - 
```
RequestSignature obj = new RequestSignature(1, "A", false, new Recipients(1, "abc@gmail.com", "A"));
try{
CloseableHttpResponse resp = obj.create_signature_templates(api_obj.base_url, api_obj.api_token);
catch(Exception e){}
```

### Node
The source code is available in `node_sample/payload/RequestSignature.js`.

Sample Example in Node -
```
rs_obj = new RequestSignature(100, new Recipients(1, "abc@xyz.com", "R"), false, "R");
rs_obj.create_signature_templates(api_obj.base_url, api_obj.api_token).then((body) =>
console.log("success", body)).catch((error) => console.log("error", error))
```

##3- Fetch embedded sending url
### Python
The source code is available in `python_sample/payloads/embedded_sending_url.py`.

Sample Example in Python - 
```
obj = SendingUrl(file_id=1245550, recipients=[Recipients(first_name="xyz", email="a.b@c.com", role_id=1)])
resp, code = obj.fetch_embedded_sending_url(api_obj.headers, api_obj.base_url)    # This should return json, status code
```

### Java
The source code is available in `java_samples/payloads/SendingUrl.java`.

Sample Example in Java - 
```
SendingUrl obj = new SendingUrl("1245550", new Recipients(1, "a.b@c.com", "A"));
try{
CloseableHttpResponse resp = obj.fetch_embedded_sending_url(api_obj.base_url, api_obj.api_token);
catch(Exception e){}
```

### Node
The source code is available in `node_sample/payload/SendingUrl.js`.

Sample Example in Node -
```
obj = new SendingUrl("1245550", new Recipients(1, "abc@xyz.com", "R"));
obj.fetch_embedded_sending_url(api_obj.base_url, api_obj.api_token).then((body) =>
console.log("success", body)).catch((error) => console.log("error", error));
```


##4- Upload file
### Python
The source code is available in `python_sample/payloads/upload_file.py`.

Sample Example in Python - 
```
obj = UploadFile(name="demo.txt", file="/Users/demo/project/api-samples/python_sample/demo.txt")
resp, code = obj.upload_file(api_obj.headers, api_obj.base_url)    # This should return json, status code
```

### Java
The source code is available in `java_samples/payloads/UploadFile.java`.

Sample Example in Java - 
```
UploadFile obj = new UploadFile("demo.txt", "/Users/demo/project/api-samples/python_sample/demo.txt");
try{
CloseableHttpResponse resp = obj.upload_file(api_obj.base_url, api_obj.api_token);
catch(Exception e){}
```

### Node
The source code is available in `node_sample/payload/UploadFile.js`.

Sample Example in Node -
```
obj = new UploadFile("demo.txt", "/Users/demo/project/api-samples/python_sample/demo.txt");
obj.upload_file(api_obj.base_url, api_obj.api_token).then((body) =>
console.log("success", body)).catch((error) => console.log("error", error));
```


##5- Create a signature request with fields
### Python
The source code is available in `python_sample/payloads/request_signature_with_fields.py`.

Sample Example in Python - 
```
obj = RequestSignaturesWithFields(original_file_id=38814455,is_ordered=False, name="me",
                                  recipients=[Recipients(first_name="xyz", email="a.b@c.com", role_id=1)],
                                  fields_payload=[FieldsPayload(email="a.b@c.com", type="text", page_number=1,
                                                                x=10, y=10, width=20, height=20)])
resp, code = obj.create_signature_request(api_obj.headers, api_obj.base_url)    # This should return json, status code
```

### Java
The source code is available in `java_samples/payloads/RequestSignatureWithFields.java`.

Sample Example in Java - 
```
RequestSignatureWithFields obj = new RequestSignatureWithFields(38814455, new Recipients(1, "abc@gmail.com", "abc@gmail.com"),
	                                       false, "a", new FieldsPayload("abc@gmail.com", "text", 1, 10,10, 20,20));
try{
CloseableHttpResponse resp = obj.create_signature_requests(api_obj.base_url, api_obj.api_token);
catch(Exception e){}
```

### Node
The source code is available in `node_sample/payload/RequestSignatureWithFields.js`.

Sample Example in Node -
```
obj = new RequestSignatureWithFields(38814455,  new Recipients(1, "a.b@c.com", "a.b@c.com"),
                                  false, "a", new FieldsPayload("a.b@c.com", "text", 1, 10,10, 20,20));
obj.create_signature_requests(api_obj.base_url, api_obj.api_token).then((body) =>
console.log("success", body)).catch((error) => console.log("error", error));
```


##6- Fetch embedded signing url
### Python
The source code is available in `python_sample/payloads/embedded_signing_url.py`.

Sample Example in Python - 
```
obj = SigningUrl(id=1234, recipient_email="a.b@c.com")
resp, code = obj.fetch_embedded_signing_url(api_obj.headers, api_obj.base_url)    # This should return json, status code
```

### Java
The source code is available in `java_samples/payloads/SigningUrl.java`.

Sample Example in Java - 
```
SigningUrl obj = new SigningUrl(1245550, "abc.cde@gmail.com");
try{
CloseableHttpResponse resp = obj.fetch_embedded_signing_url(api_obj.base_url, api_obj.api_token);
catch(Exception e){}
```

### Node
The source code is available in `node_sample/payload/SigningUrl.js`.

Sample Example in Node -
```
obj = new SigningUrl(1249790, "a.b@c.com");
obj.fetch_embedded_signing_url(api_obj.base_url, api_obj.api_token).then((body) =>
console.log("success", body)).catch((error) => console.log("error", error));
```