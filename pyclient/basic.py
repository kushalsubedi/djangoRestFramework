import requests

endpoint ="http://localhost:8000/api/"

get_response = requests.get(endpoint,json={"title":"hello", "content" : "helloworld"})


print (get_response.json())