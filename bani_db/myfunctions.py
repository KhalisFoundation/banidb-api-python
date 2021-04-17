import requests
response= requests.get("https://api.banidb.com/v2/api-docs/")
print(response)

def search(query):
    