from flask import request, appcontext_pushed, g
from contextlib import contextmanager
import server
import pytest


server.app.config["TESTING"] = True
client = server.app.test_client()


@pytest.fixture
def clubs():
    clubs = server.clubs = [
    {
        "name":"Test",
        "email":"test@test.com",
        "points":"20"
    }
    ]
    yield clubs


@pytest.fixture
def competitions():
    competitions = server.competitions = [
        {
            "name": "Test Festival 2018",
            "date": "2018-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Test Festival_2025",
            "date": "2025-03-27 10:00:00",
            "numberOfPlaces": "25"
        }
        ]
    yield competitions
    

def test_check_if_a_user_exists(clubs):
    """
    GIVEN a email
    WHEN a user try to connet with this email
    THEN check if the email exists, and redirect the user
    """

    response = client.post("/showSummary", data=clubs[0])
    assert response.status_code == 200
    assert b"test@test.com" in response.data


def test_check_if_a_user_doesnt_exists():
    """
    GIVEN a email
    WHEN a user try to connet with this email
    THEN check if the email exists, and redirect the user
    """

    response = client.post("/showSummary", data={'email': 'email@doesntexist.com'})
    assert response.status_code == 302


def test_index_url_is_online():
    """
    GIVEN a request on the index page
    WHEN the '/' page get the request (GET)
    THEN check is the status code returned is 200    
    """
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data
    assert b"Please enter your secretary email to continue:" in response.data
    assert b"To the clubs display board" in response.data


def test_competition_booking_url_is_online(competitions):

    with client as c:
        response = c.get("/book/Test%20Festival_2025/Test")
        assert response.status_code == 200
        assert b"Test Festival 2025"


def test_booking_a_competition(clubs, competitions):
    
    with client as c:
        form_data = request.form["places"]
        response = c.post("/purchasePlaces", data=form_data)
        assert response.status_code == 200



