import requests

url = "http://localhost:8000/api/recipes/1/create-review/"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU0NjA1MDIxLCJpYXQiOjE3NTQ2MDQxMjEsImp0aSI6IjJkZDRjMThmMTMyNTQwMTQ4MDBmNTZkYzgyYWU2MDMwIiwidXNlcl9pZCI6IjcifQ.3WXAb1oSopZHK74gHz4xN_-6YJ1ZUHxEJwSsR8B_4Mg",
    "Content-Type": "application/json"
}
data = {
    "rating": 5,
    "text": "This recipe was amazing!"
}

response = requests.post(url, json=data, headers=headers)
print(response.json())