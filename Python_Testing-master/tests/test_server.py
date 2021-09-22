from flask.app import Flask
import server



def test_showSummary():
    """
    GIVEN a email
    WHEN a user try to connet with this email
    THEN check if the email exists, and redirect the user
    """
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = "/"


    email = 