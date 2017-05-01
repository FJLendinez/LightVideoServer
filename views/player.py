import os
from flask import Blueprint, render_template, send_from_directory

app_player = Blueprint('player',__name__)


@app_player.route("/player/<string:vfile>")
def player(vfile):
    return render_template('player.html', vfile=vfile)


@app_player.route("/get/<string:vfile>")
def source(vfile):
    return send_from_directory(os.path.join(os.getcwd(), 'video'), vfile)