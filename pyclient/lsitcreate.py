from turtle import title
import requests

endpoint ="http://localhost:8000/api/products/"
data ={
    'title':"this field is Done "
}

get_response = requests.get(endpoint)
for i in get_response.json():
    print (i,end="\n")