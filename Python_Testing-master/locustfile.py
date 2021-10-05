import time
from locust import HttpUser, task, between


class LocustTest(HttpUser):
    wait_time = between(1, 3)

    @task
    def index(self):
        self.client.get("http://127.0.0.1:5000")

    @task
    def competition_booking_url_is_online(self):
        self.client.get("http://127.0.0.1:5000/book/Spring%20Festival/Simply%20Lift")
       
    @task
    def test_booking_a_competition(self):
        self.client.post("http://127.0.0.1:5000/purchasePlaces", data={"places": "5"})

    def on_start(self):
        self.client.post("http://127.0.0.1:5000/showSummary", data={'email': 'test@test.com'})
    
        






# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/showSummary',methods=['POST'])
# def showSummary():
#     try:
#         club = [club for club in clubs if club['email'] == request.form['email']][0]
#     except IndexError:
#         return redirect(url_for('index'))
#     else:
#         return render_template('welcome.html',club=club, competitions=competitions)
          

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


# @app.route('/purchasePlaces',methods=['POST'])
# def purchasePlaces():
   
#     competitions_list = []
#     for comp in competitions:
#         if comp['name'] == request.form['competition']:
#             competitions_list.append(comp)
#     competition = competitions_list[0]
   
#     clubs_list = []
#     for clb in clubs:
#         if clb['name'] == request.form['club']:
#             clubs_list.append(clb)
#     club = clubs_list[0]
    
#     placesRequired = int(request.form['places'])  # correspond au nombres de places voulues entrées dans le formulaire
    
#     global places_booked_counter
#     places_booked_counter += int(request.form['places'])

#     if places_booked_counter > 12 :
#         flash("You can't book more than 12 places in a competition")
#     elif int(request.form['places']) > int(club["points"]):
#         flash("You don't have enough points")
#     else:
#         competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
#         club["points"] = int(club["points"]) - placesRequired     
#         flash('Great-booking complete!')
#     return render_template('welcome.html', club=club, competitions=competitions)

# # Ils devraient voir un message confirmant le nombre de places achetées, ou un
# # message indiquant que le concours est complet. Les points utilisés doivent être
# # déduits du total précédent.


# @app.route('/board')
# def board():
#     return render_template('board.html',clubs=clubs)


# @app.route('/logout')
# def logout():
#     return redirect(url_for('index'))