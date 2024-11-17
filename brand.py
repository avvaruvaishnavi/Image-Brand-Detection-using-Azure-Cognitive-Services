from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import cred

url=cred.url
key=cred.key

con=ComputerVisionClient(url,CognitiveServicesCredentials(key))

img="https://www.teez.in/cdn/shop/products/Microsoft-Logo-T-Shirt-For-Men_s-2_large.jpg?v=1587351812"
feature= ["brands"]

res =con.analyze_image(img,feature)

if len(res.brands)==0:
    print("no brand was found in this img")
else:
    for brand in res.brands:
        print(brand.name,"----------",brand.confidence*100)
