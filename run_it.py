import os
from flask import Flask, redirect
from views.list import app_list
from views.player import app_player
from views.uploader import app_uploader


app = Flask(__name__)
app.register_blueprint(app_list)
app.register_blueprint(app_player)
app.register_blueprint(app_uploader)

@app.route("/")
def main():
    return redirect("/list")

if __name__ == "__main__":
    if os.path.exists(os.path.join(os.getcwd(),'video')):
        print("Video folder already exists")
    else:
        print("Creating video folder on "+os.path.join(os.getcwd(),'video'))
        os.mkdir(os.path.join(os.getcwd(),'video'))
    app.config.from_pyfile("./instance/local.py")
    app.run(host='0.0.0.0',port=80)
