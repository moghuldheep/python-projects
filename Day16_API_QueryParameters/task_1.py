import requests

url = "https://jsonplaceholder.typicode.com/users"

user_id = int(input("Enter the userid to search for: "))

params = {
        "id" : user_id
        }

response = requests.get(url, params=params)

try:
    response.raise_for_status()

    data = response.json()

    print(response.status_code)
    print(data)
    print(url)
except requests.exceptions.RequestException as e:
    print(f"Unable to fetch {url}: {e}")

