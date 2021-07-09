# OCR - Eden AI API
## Description
This repositery provides code to implement Eden AI OCR API. Eden AI OCR API allows to call OCR APIs from multpile OCR providers. It permits to get results from these providers, compare the results, siwtch between providers or combine them.

## What is AI-Compare ?
[Eden AI](https://www.edanai.co/) is a SaaS providing APIs connected to big (AWS, GCP, etc.) and small AI providers for vision, text, audio, OCR, prediction and translation AI engines. Our solution allows users to compare the performance of these providers APIs according to their data and use them directly via our API thus offering great flexibility and making it very easy to change supplier. In particular, we offer better performance with the "Genius" feature that cleverly combines results from multiple providers.

Eden AI offers community offer (free) when you [create your account for free](https://app.edenai.run/user/login). You can then use [APIs](https://api.edenai.run/v1/redoc/), use the [interface](https://app.edenai.run/bricks/default), manage your account, access to cost management.

You can find APIs documentation here : https://api.edenai.run/v1/redoc/

## Usage
### Initialization
Enter your access token and select your API endpoint. You can get your token on your IAM [here](https://app.edenai.run/admin/user).
```python
import requests
headers = {  'Authorization': 'Bearer your API Key'}
url = 'https://dev-api.edenai.run/v1/pretrained/vision/ocr'
```
### Select parameters 
Set your file (.jpg, .png, .jpeg, .pdf, .tiff), the language of the text searched, the attempted text, and providers APIs you want to run :
```python
payload = {'providers': '[\'ocr_space\', \'cognitives_service\', \'aws\', \'google_cloud\']','text_reference': '','language': 'French'}
files = [  ('files', open('Picture/example.jpg','rb'))]
```
### Get results
```python
response = requests.request("POST", url, headers=headers, data = payload, files = files)
print(response.text.encode('utf8'))
```

## Response example
<details>
<summary>

```json
  "result": {
    "Ocr Space": {
      "execution_time": "2.70642",
      "final_text": "A Simple PDF File  This is a small demonstration _pdf file -  just for use in the Virtual Mechanics tutoria15 More text. And more  text And more text. And more text And more text  And more text. And more text And more text. And more text. And more  text And more text. Boring: zzzzz And more text. And more text And  more text And more text. And more text And more text And more text.  And more text. And more text  And more text. And more text And more text. And more text. And more  text And more text. And more text Even more. Continued on page 2  Simple PDF File 2  .continued from page 1. Yet more text And more text. And more text  And more text. And more text And more text And more text. And more  text Oh, how boring typing this stuff. But not as boring as watching  paint dry. And more text And more text. And more text And more text.  Borin$ More, a little more text The end: and just as well.",
      "matching_characters": 440,
      "pricing": "~ $0.00020 per page",
```

</summary>

```json
"result": {
    "Ocr Space": {
      "execution_time": "2.70642",
      "final_text": "A Simple PDF File  This is a small demonstration _pdf file -  just for use in the Virtual Mechanics tutoria15 More text. And more  text And more text. And more text And more text  And more text. And more text And more text. And more text. And more  text And more text. Boring: zzzzz And more text. And more text And  more text And more text. And more text And more text And more text.  And more text. And more text  And more text. And more text And more text. And more text. And more  text And more text. And more text Even more. Continued on page 2  Simple PDF File 2  .continued from page 1. Yet more text And more text. And more text  And more text. And more text And more text And more text. And more  text Oh, how boring typing this stuff. But not as boring as watching  paint dry. And more text And more text. And more text And more text.  Borin$ More, a little more text The end: and just as well.",
      "matching_characters": 440,
      "pricing": "~ $0.00020 per page",
      "api_response": {
        "ParsedResults": [
          {
            "TextOverlay": {
              "Lines": [],
              "HasOverlay": false,
              "Message": "Text overlay is not provided as it is not requested"
            },
            "TextOrientation": "0",
            "FileParseExitCode": 1,
            "ParsedText": "A Simple PDF File\r\nThis is a small demonstration _pdf file -\r\njust for use in the Virtual Mechanics tutoria15 More text. And more\r\ntext And more text. And more text And more text\r\nAnd more text. And more text And more text. And more text. And more\r\ntext And more text. Boring: zzzzz And more text. And more text And\r\nmore text And more text. And more text And more text And more text.\r\nAnd more text. And more text\r\nAnd more text. And more text And more text. And more text. And more\r\ntext And more text. And more text Even more. Continued on page 2\r\n",
            "ErrorMessage": "",
            "ErrorDetails": ""
          },
          {
            "TextOverlay": {
              "Lines": [],
              "HasOverlay": false,
              "Message": "Text overlay is not provided as it is not requested"
            },
            "TextOrientation": "0",
            "FileParseExitCode": 1,
            "ParsedText": "Simple PDF File 2\r\n.continued from page 1. Yet more text And more text. And more text\r\nAnd more text. And more text And more text And more text. And more\r\ntext Oh, how boring typing this stuff. But not as boring as watching\r\npaint dry. And more text And more text. And more text And more text.\r\nBorin$ More, a little more text The end: and just as well.\r\n",
            "ErrorMessage": "",
            "ErrorDetails": ""
          }
        ],
        "OCRExitCode": 1,
        "IsErroredOnProcessing": false,
        "ProcessingTimeInMilliseconds": "359",
        "SearchablePDFURL": "Searchable PDF not generated as it was not requested."
      }
    },
    "Amazon Web Services": {
      "execution_time": "11.453142",
      "final_text": "A Simple PDF File This is a small demonstration .pdf file just for use in the Virtual Mechanics tutorials. More text. And more text. And more text And more text. And more text. And more text. And more text And more text And more text. And more text. And more text. A Simple PDF File This is a small demonstration .pdf file just for use in the Virtual Mechanics tutorials. More text. And more text. And more text And more text. And more text. And more text. And more text And more text And more text. And more text. And more text. Simple PDF File 2 ...continued from page 1. Yetmore text. And more text And more text. And more text And more text. And more And text. how stuff. text. more text. And more Oh, boring typing this not boring as watching paint dry. And more text. And more text. And more text Simple PDF File 2 ...continued from page 1. Yetmore text. And more text And more text. And more text And more text. And more text. And more text. And more text. Oh, how boring typing this stuff. not boring as watching paint dry. And more text. And more text. And more text",
      "matching_characters": 217,
      "pricing": "$0.0006 per page",
      "api_response": [
        {
          "TextDetections": [
            {
              "DetectedText": "A Simple PDF File",
              "Type": "LINE",
              "Id": 0,
              "Confidence": 99.74014282226562,
              "Geometry": {
                "BoundingBox": {
                  "Width": 0.365053653717041,
                  "Height": 0.03881004825234413,
                  "Left": 0.09998568147420883,
                  "Top": 0.056453362107276917
                },
                "Polygon": [
                  {
                    "X": 0.09998568147420883,
                    "Y": 0.056453362107276917
                  },
                  {
                    "X": 0.46503934264183044,
                    "Y": 0.05493946000933647
                  },
                  {
                    "X": 0.46530890464782715,
                    "Y": 0.0937495082616806
                  },
                  {
                    "X": 0.10025525093078613,
                    "Y": 0.09526340663433075
                  }
                ]
              }
            },
            {
              "DetectedText": "This is a small demonstration .pdf file",
              "Type": "LINE",
              "Id": 1,
              "Confidence": 97.49700164794922,
              "Geometry": {
                "BoundingBox": {
                  "Width": 0.28058895468711853,
                  "Height": 0.01657564751803875,
                  "Left": 0.11261451244354248,
                  "Top": 0.11627907305955887
                },
                "Polygon": [
                  {
                    "X": 0.11261451244354248,
                    "Y": 0.11627907305955887
                  },
                  {
                    "X": 0.3932034969329834,
                    "Y": 0.11619863659143448
                  },
                  {
                    "X": 0.3932114541530609,
                    "Y": 0.13277429342269897
                  },
                  {
                    "X": 0.11262247711420059,
                    "Y": 0.13285471498966217
                  }
                ]
              }
            },
            {
              "DetectedText": "just for use in the Virtual Mechanics tutorials. More text. And more",
              "Type": "LINE",
              "Id": 2,
              "Confidence": 96.80105590820312,
              "Geometry": {
                "BoundingBox": {
                  "Width": 0.47961172461509705,
                  "Height": 0.014284299686551094,
                  "Left": 0.11456143110990524,
                  "Top": 0.14703676104545593
                },
                "Polygon": [
                  {
                    "X": 0.11456143110990524,
                    "Y": 0.14703676104545593
                  },
                  {
                    "X": 0.5941731929779053,
                    "Y": 0.147003173828125
                  },
                  {
                    "X": 0.594174861907959,
                    "Y": 0.16128747165203094
                  },
                  {
                    "X": 0.11456310749053955,
                    "Y": 0.16132105886936188
                  }
                ]
              }
            },
            {
              "DetectedText": "text. And more text And more text. And more text.",
              "Type": "LINE",
              "Id": 3,
              "Confidence": 96.25338745117188,
              "Geometry": {
                "BoundingBox": {
                  "Width": 0.3669905662536621,
                  "Height": 0.01283635850995779,
                  "Left": 0.1135868951678276,
                  "Top": 0.1627907007932663
                },
                "Polygon": [
                  {
                    "X": 0.1135868951678276,
                    "Y": 0.1627907007932663
                  },
                  {
                    "X": 0.4805774688720703,
                    "Y": 0.16269904375076294
                  },
                  {
                    "X": 0.4805828332901001,
                    "Y": 0.1755353957414627
                  },
                  {
                    "X": 0.11359226703643799,
                    "Y": 0.17562705278396606
                  }
                ]
              }
            },
            {
              "DetectedText": "And more text. And more text And more text And more text. And more",
              "Type": "LINE",
              "Id": 4,
              "Confidence": 96.24824523925781,
              "Geometry": {
                "BoundingBox": {
                  "Width": 0.5174855589866638,
                  "Height": 0.013632897287607193,
                  "Left": 0.1145632266998291,
                  "Top": 0.19263650476932526
                },
                "Polygon": [
                  {
                    "X": 0.1145632266998291,
                    "Y": 0.19263650476932526
                  },
                  {
                    "X": 0.6320487856864929,
                    "Y": 0.19286511838436127
                  },
                  {
                    "X": 0.6320387125015259,
                    "Y": 0.20649801194667816
                  },
                  {
                    "X": 0.11455313861370087,
                    "Y": 0.20626939833164215
                  }
                ]
              }
            },
            {
              "DetectedText": "text. And more text.",
```

</details>


## Blog articles
We provides on our website some [blog articles on AI engines](https://www.edenai.co/blog)

## Contact
If you have any question or request, you can contact us at contact@edenai.com

## Terms of use
You can access to our terms [here](https://www.edenai.co/terms) on our website.

#
![Screenshot](https://github.com/ai-compare/Speech_to_text-API/blob/ba9d4f1668d8758141f24240d1287640b4211c63/Logo%20complet%20Eden%20AI%20-%20format%20PNG.png)
