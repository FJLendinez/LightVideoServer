import os
from flask import Blueprint, render_template, request, flash, redirect

app_uploader = Blueprint('uploader', __name__)

ALLOWED_EXTENSIONS = set(['mp4'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app_uploader.route("/uploader", methods=["GET", "POST"])
def uploader():
    if request.method == "GET":
        return render_template('uploader.html')
    else:
        if 'vfile' not in request.files:
            flash('No file part')
            return redirect(request.url)
        vfile = request.files['vfile']
        if vfile.filename == '':
            print('No selected file')
            return redirect(request.url)
        if vfile and allowed_file(vfile.filename):
            vfile.save(os.path.join(os.getcwd(), 'video', vfile.filename))
            return redirect("/list")