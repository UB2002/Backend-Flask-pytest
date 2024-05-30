import pytest
from app import create_app, db
from app.model import User


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    yield app


@pytest.fixture
def database(app):
    with app.app_context():
        db.create_all()
        yield db
        db.drop_all()


def test_create_test_instance(app, database):
    test_instance = User(username='test_user', email='test@example.com')
    database.session.add(test_instance)
    database.session.commit()
    queried_test_instance = User.query.filter_by(username='test_user').first()
    assert queried_test_instance is not None
    assert queried_test_instance.username == 'test_user'
    assert queried_test_instance.email == 'test@example.com'


def test_test_model_repr():
    test_instance = User(username='test_user', email='test@example.com')
    assert repr(test_instance) == "<Test 'test_user'>"
