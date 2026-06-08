import requests
import json

# Test login endpoint
url = "http://localhost:8000/api/auth/login/"
data = {
    "email": "admin@example.com",
    "password": "admin123"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=data, headers=headers)
print(f"Status: {response.status_code}")
print(f"Response: {response.text}")
