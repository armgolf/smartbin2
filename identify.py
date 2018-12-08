import requests
import os

url = 'https://app.nanonets.com/api/v2/ImageCategorization/LabelFile/'

files = (os.listdir("/home/pi/Documents/smartbin2/smartbin2-master/images"))
lastfile = files[-1]

data = {'file': open('/home/pi/Documents/smartbin2/smartbin2-master/images/'+lastfile, 'rb'), 'modelId': ('', 'febf1ef2-559e-4877-9803-ddf4247155e5')}
#data = {'file': open('./images/image2.jpg', 'rb'), 'modelId': ('', 'febf1ef2-559e-4877-9803-ddf4247155e5')}

response = requests.post(url, auth= requests.auth.HTTPBasicAuth('GvqHLwBkqU4tpSyXDU471CG6K1y5XYw8', ''), files=data)

print(response.text)

import json
data = json.loads(response.text)
a = data["result"][0]["prediction"][0]["label"]
print(a)

#You can encode the response text into json format using json.loads() function. After that, you can iterate over array to get label with maximum probability.

#{
#"message": "Prediction successful",
#"model_id": "00000000-0000-0000-0000-000000000000",
#"result": [
#{
#"input": "string",
#"prediction": [
#{
#"category": "category1",
#"probability": 0.9
#},
#{
#"category": "category2",
#"probability": 0.1
#}
#]
#}
#]
#}
