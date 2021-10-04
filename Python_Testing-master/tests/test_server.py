from flask import request, appcontext_pushed, g
from contextlib import contextmanager
import server
import pytest


server.app.config["TESTING"] = True
client = server.app.test_client()


server.clubs = [
    {
        "name":"Test",
        "email":"test@test.com",
        "points":"20"
    }
]

server.competitions = [
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


def test_check_if_a_user_exists():
    """
    GIVEN a email
    WHEN a user try to connet with this email
    THEN check if the email exists, and redirect the user
    """

    response = client.post("/showSummary", data={'email': 'test@test.com'})
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


def test_competition_booking_url_is_online():

    with client as c:
        response = c.get("/book/Test%20Festival_2025/Test")
        assert response.status_code == 200
        assert b"Test Festival 2025"


def test_booking_a_competition():
    # with client as c:
    response = client.post("/purchasePlaces", data={"places": "5"})
    # assert response.status_code == 200
    # assert b"Great-booking complete!" in response.data


# @app.route('/book/<competition>/<club>')
# def book(competition, club):

#     clubs_list = []
#     for clb in clubs:
#         if clb['name'] == club:
#             clubs_list.append(clb)
#     foundClub = clubs_list[0]

#     competitions_list = []
#     for cmp in competitions:
#         if cmp['name'] == competition:
#             competitions_list.append(cmp)
#     foundCompetition = competitions_list[0]
    
#     if foundClub and foundCompetition:
#         return render_template('booking.html', club=foundClub, competition=foundCompetition)
#     else:
#         flash("Something went wrong-please try again")
#         return render_template('welcome.html', club=club, competitions=competitions)


# @pytest.fixture
# def mock_loadClubs(mock):
#     mock.patch('server.loadClubs', return_value="Toto")

# @pytest.fixture
# def mock_loadCompetitions(mock):
#     mock.patch('server.loadClubs', return_value="Toto")


    # monkeypatch.setattr("clubs.json", "tests.mock_clubs.json")

    # result = showSummary()
    # assert result == redirect to "welcome.html"


    # with open('mock_competitions.json') as comps:
    #     listOfCompetitions = json.load(comps)['competitions']
    # return listOfCompetitions


# mock_competitions = mock_loadCompetitions()
# mock_clubs = mock_loadClubs()

# @pytest.fixture
# def client():
#     app = create_app({'TESTING': True})

#     with app.test_client() as client:
#         with app.app_context():
#             yield client


