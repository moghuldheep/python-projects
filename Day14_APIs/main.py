import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print(response.status_code)

data = response.json()
print("Datatype of data: ", type(data))

print(data[0]["name"])
print(data[0]["email"])
print(data[0]["phone"])

for user in data:
    print("====================")
    print("User ID: ", user["id"])
    print("Name: ", user["name"])
    print("Email: ", user["email"])
    print("Phone: ", user["phone"])
    print("====================")
