# Backend

## One Time Setup

- Ensure you are using Python 3.12, as 3.13 is not supported on certain ML platforms. You can use a tool like [pyenv](https://github.com/pyenv/pyenv) to switch your python version. 
- Create a virtual environment with `python3 -m venv .env`, and activate it. If you use a different name for your env, add it to `.gitignore`
  - MacOS: `source .env/bin/activate`
  - Windows: `.\venv\Scripts\activate`
- Install dependencies with `pip install -r requirements.txt`
- Run the backend with `flask -A app run --host=0.0.0.0 --port=5001` 
  - The `host` argument allows you to connect to your API from other devices on the same network, such as your phone
  - The port is set to 5001 as Airdrop runs on 4000.

## Development

### Connecting to the backend

- Get your computers local IP:
  - MacOS: `ipconfig getifaddr en0`
  - Windows: `ipconfig` and look for the `IPv4` address
- Test your connection with `http://[LOCAL IP]:5001/test`. You should get a JSON payload confirming it works.
- NOTE - this is a work around unless we get a domain/hosting solution. We will want to set a constant for the value in the frontend code. For class demos, we would need to use someones phone as a hotspot to which the phone/computer are connected to, or do our demo online.

### House Keeping

- If you add another package, be sure to perform `pip freeze > requirements.txt` to update dependencies

## API Documentation

### **Upload Image API**

`POST /api/upload-image` 

Endpoint where image will be uploaded to. Optional `test` query parameter provided for testing/mocking out backend behavior.

#### **Headers**
| Key           | Value               |
|---------------|---------------------|
| `Content-Type` | `multipart/form-data` |

#### **Body Parameters**
| Parameter | Type | Required | Description                  |
|-----------|------|----------|------------------------------|
| `image`   | `file` | Yes      | The image file to be uploaded |

#### **Query Parameters**
| Parameter | Type   | Value     | Description                                                      |
|-----------|--------|-----------|------------------------------------------------------------------|
| `test`    | `string` | `success` | Verify that the image has been attached without processing.        |
|           |          | `notfound` | Automatically return a 404 response.                            |
|           |          | `error`    | Automatically return a 500 response.                            |
|           |           | `None`    | The API functions as normal.            |

---



#### **Status Code: 200 OK**
```json
{
  "title": "String",
  "subtitle": "String",
  "author": "String",
  "rating": "number",
  "length": "number",
  "categories": "String",
  "description": "String"
}
