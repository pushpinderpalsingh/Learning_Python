import requests
import json 

subs_key = "cf229a23c3054905b5a8ad512edfa9dd"

vision_add = "https://canadacentral.api.cognitive.microsoft.com/vision/v2.0/"

address  = vision_add + "analyze"

parameters  = {'visualFeatures':'Description,Color',
               'language':'en'}
image_path = "./Parliament_Hill.jpg"
image_data = open(image_path, "rb").read()

headers    = {'Content-Type': 'application/octet-stream',
              'Ocp-Apim-Subscription-Key': subs_key}

response = requests.post(address, headers=headers, params=parameters, data=image_data)
response.raise_for_status()
results = response.json()

# print(json.dumps(results))

print(results['color']['dominantColorBackground'])

for item in results["description"]["tags"]:
        print(item)