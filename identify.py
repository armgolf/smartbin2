import requests

url = 'https://app.nanonets.com/api/v2/ImageCategorization/LabelFile/'

data = {'file': open('/home/pi/Documents/Smartbin/image.jpg', 'rb'), 'modelId': ('', 'febf1ef2-559e-4877-9803-ddf4247155e5')}

response = requests.post(url, auth= requests.auth.HTTPBasicAuth('GvqHLwBkqU4tpSyXDU471CG6K1y5XYw8', ''), files=data)

print(response.text)
