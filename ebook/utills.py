
import requests
import uuid
import json

def clean_string(input_string):
    # Convert the string to lowercase
    input_string = input_string.lower()

    # Remove whitespace characters
    input_string = input_string.replace(" ", "")

    # Return the cleaned string
    return str(input_string)



def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4())  # Convert UUID format to a Python string.
    random = random.lower()  # Make all characters uppercase.
    random = random.replace("-", "")  # Remove the UUID '-'.
    # usage  = '%s-%s'%('TR',my_random_string(6))
    return random[0:string_length]  # Return the random string.
    
def get_site_id(name):
    url = "https://api.swiftxr.io/v1/sites"

    payload = json.dumps({
    "site_name": clean_string(name),
    "config": {
        "type": "model",
        "logo_url": "",
        "compress_model": True,
        "model_compression_level": 5,
        "compress_image": True,
        "image_compression_level": 5,
        "use_ar": False
    }
    })
    headers = {
    'Authorization': 'Bearer SWF.8OEDftHHfg4jPA.szwPDnyEjnHFf8KcOurylnRuFUHbMOQ0nx7rpAFwwG0',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    return json.loads(response.content)




def upload_model(file, site_id):
    url = f"https://api.swiftxr.io/v1/sites/deploy/{site_id}/"

    # Set the filename to be used in the API request
    # breakpoint()
    filename = file.name

    # Prepare the file data to be sent along with the request
    file_data = (filename, file.read(), 'application/octet-stream')

    # Set the headers to be used in the API request
    headers = {
        'Authorization': 'Bearer SWF.8OEDftHHfg4jPA.szwPDnyEjnHFf8KcOurylnRuFUHbMOQ0nx7rpAFwwG0'
    }

    # Set the payload to be used in the API request
    payload = {}

    # Set the files to be used in the API request
    files = {'deploy': file_data}

    # Send the API request
    response = requests.post(url, headers=headers, data=payload, files=files)

    return json.loads(response.content)

