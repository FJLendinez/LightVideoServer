import os
from flask import Blueprint, render_template

app_list = Blueprint('list',__name__)


@app_list.route("/list")
def list():
    return render_template('list.html', vlist=os.listdir(os.path.join(os.getcwd(),'video')))
