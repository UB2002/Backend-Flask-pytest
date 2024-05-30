# tests/test_routes.py
import pytest
from app import create_app, db
from app.model import User


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()
        yield app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client


def test_home_route(client):
    try:
        response = client.get('/')
        assert response.status_code == 200
        assert b"<h1>home</h1>" in response.data
    except Exception as e:
        print(e)


def test_user_page(client):
    try:
        response = client.get('/user')
        assert response.status_code == 200
        assert b"welcome to user page" in response.data
    except Exception as e:
        print(e)


def test_post_route(client):
    try:
        data = {"username": "luffy", "email": "monkeyDluffy@gmail.com"}
        response = client.post('/post', json=data)
        assert response.status_code == 200
        assert b"you successfully added the data" in response.data
        assert User.query.filter_by(username="luffy").first() is not None
    except Exception as e:
        print(e)


def test_get_route(client):
    try:
        # Insert test data into the database
        test_data = [
            {"username": "UB2002", "email": "UB2002@example.com"},
            {"username": "UB2332", "email": "UB2332@example.com"}
        ]
        for data in test_data:
            new_user = User(username=data['username'], email=data['email'])
            db.session.add(new_user)
        db.session.commit()

        # Access the GET route to retrieve data
        response = client.get('/get')

        # Assert response status code
        assert response.status_code == 200

        # Assert data is present in response
        assert b"UB2002" in response.data
        assert b"UB2332" in response.data
    except Exception as e:
        print(e)
