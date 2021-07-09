import requests

# You can find the documentation here : https://api.edenai.run/v1/redoc/#section/How-it-works

#Enter your API Token
headers = {'Authorization': 'Bearer your API Key'}

# Select API
url = 'https://api.edenai.run/v1/pretrained/vision/ocr'

# Select providers, and text to detect
payload = {'providers': '[\'ocr_space\', \'microsoft\', \'aws\', \'google_cloud\']','text_reference': '','language': 'French'}

# Select file to test
files = [  ('files', open('Picture/example.jpg','rb'))]

# Request to Eden AI
response = requests.request("POST", url, headers=headers, data = payload, files = files)

# Print result
print(response.text.encode('utf8'))
