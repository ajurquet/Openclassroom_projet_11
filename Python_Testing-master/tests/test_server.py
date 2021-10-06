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
    THEN check is the status code returned is 200, and if a text is in the response 
    """
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data
    assert b"Please enter your secretary email to continue:" in response.data
    assert b"To the clubs display board" in response.data


def test_competition_booking_url_is_online(competitions):
    """
    GIVEN a request on the booking page
    WHEN the '/book/<competition_name>/<club_name>' page get the request (GET)
    THEN check is the status code returned is 200, and if a text is in the response 
    """
    with client as c:
        response = c.get("/book/Test%20Festival_2025/Test")
        assert response.status_code == 200
        assert b"Test Festival 2025"


def test_booking_a_competition(clubs, competitions):
    """
    GIVEN a user filling a form to book a competition
    WHEN the '/purchasePlaces' page get the form request (POST)
    THEN check is the status code returned is 200, and if a text is in the response 
    """
    with client as c:
        response = c.post("/purchasePlaces", data={"places": "4", "club": clubs[0]["name"],
                                                    "competition": competitions[0]["name"]
                                                    })
        assert response.status_code == 200
        assert b"Great, booking complete!"


def test_booking_more_than_12_places(clubs, competitions):
    """
    GIVEN a user filling a form to book a competition, trying to book more than 12 places
    WHEN the '/purchasePlaces' page get the form request (POST)
    THEN check is the status code returned is 200, and if a text is in the response 
    """
    with client as c:
        response = c.post("/purchasePlaces", data={"places": "15", "club": clubs[0]["name"],
                                                    "competition": competitions[0]["name"]
                                                    })
        assert response.status_code == 200
        assert b"You can't book more than 12 places in a competition"


def test_board_url_is_online():
    """
    GIVEN a request on the board page
    WHEN the '/board' page get the request (GET)
    THEN check is the status code returned is 200, and if a text is in the response 
    """
    response = client.get("/board")
    assert response.status_code == 200
    assert b"GUDLFT Club's display board" in response.data
    assert b"Back to index" in response.data


def test_logout_url_redirect_to_index():
    """
    GIVEN a request on the logout page
    WHEN the '/logout' page get the request (GET)
    THEN check is the status code returned is 200, and if a text is in the response 
    """
    response = client.get("/logout")
    assert response.status_code == 302


def test_3_points_to_book_a_competition(clubs, competitions):
    """
    GIVEN a user filling a form to book a competition.
    WHEN the '/purchasePlaces' page get the form request (POST)
    THEN check is the status code returned is 200, and if it removes 3 points to the competitions points
    """
    old_clubs_points = int(clubs[0]["points"])
    
    with client as c:
        response = c.post("/purchasePlaces", data={"places": "1", "club": clubs[0]["name"],
                                                    "competition": competitions[0]["name"]
                                                    })
        assert response.status_code == 200
        assert old_clubs_points - 3 == int(clubs[0]["points"])