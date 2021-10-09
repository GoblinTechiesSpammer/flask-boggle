from boggle import Boggle
#Imported by me
from flask import Flask, request, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension

#Setup flask and flask debug toolbar
app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route("/")
def home_page():
    """Shows home page."""
    new_board = boggle_game.make_board()

    return render_template("home.html", board=new_board)