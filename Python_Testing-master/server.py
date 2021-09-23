import json
from flask import Flask, render_template, request, redirect, flash,url_for


def loadClubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
    return listOfClubs

def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
    return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary',methods=['POST'])
def showSummary():
    club = [club for club in clubs if club['email'] == request.form['email']][0]
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition, club):

    clubs_list = []
    for clb in clubs:
        if clb['name'] == club:
            clubs_list.append(clb)
    foundClub = clubs_list[0]

    competitions_list = []
    for cmp in competitions:
        if cmp['name'] == competition:
            competitions_list.append(cmp)
    foundCompetition = competitions_list[0]
    
    if foundClub and foundCompetition:
        return render_template('booking.html', club=foundClub, competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
   
    competitions_list = []
    for comp in competitions:
        if comp['name'] == request.form['competition']:
            competitions_list.append(comp)
    competition = competitions_list[0]
   
    clubs_list = []
    for clb in clubs:
        if clb['name'] == request.form['club']:
            clubs_list.append(clb)
    club = clubs_list[0]
    
    placesRequired = int(request.form['places'])  # correspond au nombres de places voulues entrées dans le formulaire

    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
    club["points"] = int(club["points"]) - placesRequired
    
    # c'est ici qu'il faut enlever des places dans le json
    
    # for clb in clubs:
    #     if clb["name"] == request.form['club']:
    with open("clubs.json", "w") as clubs_file:
        print(clubs_file)
        json.dump(clubs[0], clubs_file)

        # json.dump(club, clubs_file)

            # print(clb["name"])
            # clb["points"] = club["points"]
            # print(request.form['club'])
        
        
        # TODO chercher la ligne à mettre à jour dans le json



    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))