import requests

# You can find the documentation here : https://www.ai-compare.com/v1/redoc/#operation/OCR

#Enter your API Token
headers = {  'Authorization': 'Bearer your API Key'} #You can get your free API token here https://www.ai-compare.com/accounts/login/?next=/my_apis

# Select API
url = 'https://www.ai-compare.com/v1/pretrained/vision/ocr'

# Select providers, and text to detect
payload = {'providers': '[\'ocr_space\', \'cognitives_service\', \'aws\', \'google_cloud\']','text_reference': '','language': 'French'}

# Select file to test
files = [  ('files', open('Picture/example.jpg','rb'))]

# Request to AI COMPARE
response = requests.request("POST", url, headers=headers, data = payload, files = files)

# Print result
print(response.text.encode('utf8'))
