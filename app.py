from werkzeug.utils import redirect
from boggle import Boggle
#Imported by me
from flask import Flask, request, render_template, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

#Setup flask and flask debug toolbar
app = Flask(__name__)
app.config['SECRET_KEY'] = "test123"
debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route("/")
def home_page():
    """Shows home page."""
    board = boggle_game.make_board()
    session['board'] = board
    
    #Clear score
    session['score'] = 0

    return render_template("home.html")

@app.route("/guess")
def guess():
    """Recieve GET request from axios"""
    word = request.args["word"]
    #Already check both, even though instructions say to check each(dictionary and board) independenty.
    validity = boggle_game.check_valid_word(session['board'], word)

    #Adding word length to score.
    if validity == 'ok':
        score = session['score']
        score += len(word)
        session['score'] = score

    return jsonify({'result': validity, 'score': session['score']})