import requests

BASE_URL = "http://127.0.0.1:8000"

def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    print("✅ GET /tasks passed!")

def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    print("✅ GET /users passed!")

def test_home():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    print("✅ GET / (home) passed!")

if __name__ == "__main__":
    test_get_tasks()
    test_get_users()
    test_home()
