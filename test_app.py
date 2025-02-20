# unit testing
from app import app

def test_home():
    response=app.test_client().get("/")
    print('inside test')
    assert response.status_code==200
    assert response.data=="hello world"