from werkzeug.utils import redirect
from boggle import Boggle
#Imported by me
from flask import Flask, request, render_template, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

#Setup flask and flask debug toolbar
app = Flask(__name__)
app.config['SECRET_KEY'] = "test123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

boggle_game = Boggle()

#Tracking number of games played.
#Why can't I use session right here?

@app.route("/")
def home_page():
    """Shows home page. Initializes the boggle game."""
    initialize_game()
    return render_template("home.html")

@app.route("/guess")
def guess():
    """Recieve GET request from axios. Returns the validity of the word and the new score."""
    word = request.args["word"]
    #Already check both, even though instructions say to check each(dictionary and board) independenty.
    validity = boggle_game.check_valid_word(session['board'], word)

    #Adding word length to score if word is valid.
    if validity == 'ok':
        update_score(word)

    return jsonify({'result': validity, 'score': session['score']})

@app.route("/end")
def end():
    """Store the score, and number of times played"""
    #Update or initialize high score.
    update_high_score(request.args['high_score'])

    #Incement number of games played by 1
    update_games_played()

    return redirect("/")

#Initializes and resets the boggle game.
def initialize_game():
    board = boggle_game.make_board()
    session['board'] = board
    session['score'] = 0

#Updates the game score with the length of the word.
def update_score(word):
    score = session['score']
    score += len(word)
    session['score'] = score

#Increments the number of games of boggle played by one, initializes the number to 1 if none have been played yet.
def update_games_played():
    if 'games_played' in session:
        games_played = session['games_played']
        games_played += 1
        session['games_played'] = games_played
    else:
        session['games_played'] = 1

#Update or initailize high score.
def update_high_score(high_score):
    if 'high_score' in session:
        if int(high_score) > int(session['high_score']):
            session['high_score'] = high_score
    else:
        session['high_score'] = high_score