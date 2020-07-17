import requests

# You can find the documentation here : https://documenter.getpostman.com/view/10011301/SzmiVFqh?version=latest#971d5367-728e-49b0-954f-8debec142cf7

#Enter your API Token
headers = {  'x-access-token': 'Enter your API Key'} #You can get your free API token here https://www.ai-compare.com/accounts/login/?next=/my_apis

# Select API
url = 'https://www.ai-compare.com/api/v1/vision/create/compare/ocr'

# Select providers, and text to detect
payload = {'providers': '[\'ocr_space\', \'cognitives_service\', \'aws\']','text_reference': '','language': 'French'}

# Select file to test
files = [  ('files', open('Picture/example.jpg','rb'))]

# Request to AI COMPARE
response = requests.request("POST", url, headers=headers, data = payload, files = files)

# Print result
print(response.text.encode('utf8'))
