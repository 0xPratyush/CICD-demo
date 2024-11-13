import pytest

try:
    from app import app  # Attempt to import the Flask app
except ImportError as e:
    raise ImportError("Error importing the Flask app. Ensure Flask and Werkzeug versions are compatible.") from e

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test the main route
def test_app_is_working(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello World!" in response.data

# Additional test for the API route (if defined in app.py)
def test_api_message(client):
    response = client.get('/api/message')
    assert response.status_code == 200
    assert b"Hello from the API!" in response.data
