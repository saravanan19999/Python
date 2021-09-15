from fastapi.testclient import TestClient
from app.server.app import app
from app.server.route.student import router

client=TestClient(router)

data ={
          "fullname": "John Doe",
          "email": "jdoe@x.edu.ng",
          "course_of_study": "Water resources engineering",
          "year": 2,
          "gpa": "3.0",

}

def test_insert():
    response = client.post("/",json=data)
    assert response.status_code == 200
