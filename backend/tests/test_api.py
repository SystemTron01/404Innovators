import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test API is running
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "AI Task Allocation API is running!"}
    print("✅ GET / (home) passed!")

# Test fetching all tasks
def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert "tasks" in response.json()
    print("✅ GET /tasks passed!")

# Test fetching all users
def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert "users" in response.json()
    print("✅ GET /users passed!")

# Run all tests if script is executed directly
if __name__ == "__main__":
    pytest.main()
