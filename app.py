from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("hey.html")
@app.route("/add_one_photos", methods=["GET","POST"])
def add_one_photos():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into photos (name,pic,author_id) values (:name,:pic,:author_id)",request.form)
        user = query_db('select * from photos')
        return render_template("photosform.html", photoss=user, one_user=one_user, the_title="add new photos")
    user = query_db('select * from photos')
    one_user = query_db("select * from photos limit 1", one=True)
    return render_template("photosform.html", photoss=user, one_user=one_user, the_title="add new photos")

@app.route("/add_one_video", methods=["GET","POST"])
def add_one_video():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into video (name,vid,author_id) values (:name,:vid,:author_id)",request.form)
        user = query_db('select * from video')
        return render_template("videoform.html", videos=user, one_user=one_user, the_title="add new video")
    user = query_db('select * from video')
    one_user = query_db("select * from video limit 1", one=True)
    return render_template("videoform.html", videos=user, one_user=one_user, the_title="add new video")

@app.route("/add_one_post", methods=["GET","POST"])
def add_one_post():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into post (title,content,author_id) values (:title,:content,:author_id)",request.form)
        user = query_db('select * from post')
        return render_template("postform.html", posts=user, one_user=one_user, the_title="add new post")
    user = query_db('select * from post')
    one_user = query_db("select * from post limit 1", one=True)
    return render_template("postform.html", posts=user, one_user=one_user, the_title="add new post")

@app.route("/add_one_recording", methods=["GET","POST"])
def add_one_recording():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into recording (title,rec,author_id) values (:title,:rec,:author_id)",request.form)
        user = query_db('select * from recording')
        return render_template("recordingform.html", recordings=user, one_user=one_user, the_title="add new recording")
    user = query_db('select * from recording')
    one_user = query_db("select * from recording limit 1", one=True)
    return render_template("recordingform.html", recordings=user, one_user=one_user, the_title="add new recording")

@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into user (username,email,password,sex,photo,country_id) values (:username,:email,:password,:sex,:photo,:country_id)",request.form)
        user = query_db('select * from user')
        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")
    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")

@app.route("/add_one_photos", methods=["GET","POST"])
def add_one_photos():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into photos (name,pic,author_id) values (:name,:pic,:author_id)",request.form)
        user = query_db('select * from photos')
        return render_template("photosform.html", photoss=user, one_user=one_user, the_title="add new photos")
    user = query_db('select * from photos')
    one_user = query_db("select * from photos limit 1", one=True)
    return render_template("photosform.html", photoss=user, one_user=one_user, the_title="add new photos")

@app.route("/add_one_video", methods=["GET","POST"])
def add_one_video():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into video (name,vid,author_id) values (:name,:vid,:author_id)",request.form)
        user = query_db('select * from video')
        return render_template("videoform.html", videos=user, one_user=one_user, the_title="add new video")
    user = query_db('select * from video')
    one_user = query_db("select * from video limit 1", one=True)
    return render_template("videoform.html", videos=user, one_user=one_user, the_title="add new video")

@app.route("/add_one_post", methods=["GET","POST"])
def add_one_post():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into post (title,content,author_id) values (:title,:content,:author_id)",request.form)
        user = query_db('select * from post')
        return render_template("postform.html", posts=user, one_user=one_user, the_title="add new post")
    user = query_db('select * from post')
    one_user = query_db("select * from post limit 1", one=True)
    return render_template("postform.html", posts=user, one_user=one_user, the_title="add new post")

@app.route("/add_one_recording", methods=["GET","POST"])
def add_one_recording():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into recording (title,rec,author_id) values (:title,:rec,:author_id)",request.form)
        user = query_db('select * from recording')
        return render_template("recordingform.html", recordings=user, one_user=one_user, the_title="add new recording")
    user = query_db('select * from recording')
    one_user = query_db("select * from recording limit 1", one=True)
    return render_template("recordingform.html", recordings=user, one_user=one_user, the_title="add new recording")

@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into user (username,email,password,sex,photo,country_id) values (:username,:email,:password,:sex,:photo,:country_id)",request.form)
        user = query_db('select * from user')
        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")
    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")

@app.route("/add_one_photos", methods=["GET","POST"])
def add_one_photos():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into photos (name,pic,author_id) values (:name,:pic,:author_id)",request.form)
        user = query_db('select * from photos')
        return render_template("photosform.html", photoss=user, one_user=one_user, the_title="add new photos")
    user = query_db('select * from photos')
    one_user = query_db("select * from photos limit 1", one=True)
    return render_template("photosform.html", photoss=user, one_user=one_user, the_title="add new photos")

@app.route("/add_one_video", methods=["GET","POST"])
def add_one_video():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into video (name,vid,author_id) values (:name,:vid,:author_id)",request.form)
        user = query_db('select * from video')
        return render_template("videoform.html", videos=user, one_user=one_user, the_title="add new video")
    user = query_db('select * from video')
    one_user = query_db("select * from video limit 1", one=True)
    return render_template("videoform.html", videos=user, one_user=one_user, the_title="add new video")

@app.route("/add_one_post", methods=["GET","POST"])
def add_one_post():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into post (title,content,author_id) values (:title,:content,:author_id)",request.form)
        user = query_db('select * from post')
        return render_template("postform.html", posts=user, one_user=one_user, the_title="add new post")
    user = query_db('select * from post')
    one_user = query_db("select * from post limit 1", one=True)
    return render_template("postform.html", posts=user, one_user=one_user, the_title="add new post")

@app.route("/add_one_recording", methods=["GET","POST"])
def add_one_recording():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into recording (title,rec,author_id) values (:title,:rec,:author_id)",request.form)
        user = query_db('select * from recording')
        return render_template("recordingform.html", recordings=user, one_user=one_user, the_title="add new recording")
    user = query_db('select * from recording')
    one_user = query_db("select * from recording limit 1", one=True)
    return render_template("recordingform.html", recordings=user, one_user=one_user, the_title="add new recording")

@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into user (username,email,password,sex,photo,country_id) values (:username,:email,:password,:sex,:photo,:country_id)",request.form)
        user = query_db('select * from user')
        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")
    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")

@app.route("/add_one_photos", methods=["GET","POST"])
def add_one_photos():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into photos (name,pic,author_id) values (:name,:pic,:author_id)",request.form)
        user = query_db('select * from photos')
        return render_template("photosform.html", photoss=user, one_user=one_user, the_title="add new photos")
    user = query_db('select * from photos')
    one_user = query_db("select * from photos limit 1", one=True)
    return render_template("photosform.html", photoss=user, one_user=one_user, the_title="add new photos")

@app.route("/add_one_video", methods=["GET","POST"])
def add_one_video():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into video (name,vid,author_id) values (:name,:vid,:author_id)",request.form)
        user = query_db('select * from video')
        return render_template("videoform.html", videos=user, one_user=one_user, the_title="add new video")
    user = query_db('select * from video')
    one_user = query_db("select * from video limit 1", one=True)
    return render_template("videoform.html", videos=user, one_user=one_user, the_title="add new video")

@app.route("/add_one_post", methods=["GET","POST"])
def add_one_post():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into post (title,content,author_id) values (:title,:content,:author_id)",request.form)
        user = query_db('select * from post')
        return render_template("postform.html", posts=user, one_user=one_user, the_title="add new post")
    user = query_db('select * from post')
    one_user = query_db("select * from post limit 1", one=True)
    return render_template("postform.html", posts=user, one_user=one_user, the_title="add new post")

@app.route("/add_one_recording", methods=["GET","POST"])
def add_one_recording():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into recording (title,rec,author_id) values (:title,:rec,:author_id)",request.form)
        user = query_db('select * from recording')
        return render_template("recordingform.html", recordings=user, one_user=one_user, the_title="add new recording")
    user = query_db('select * from recording')
    one_user = query_db("select * from recording limit 1", one=True)
    return render_template("recordingform.html", recordings=user, one_user=one_user, the_title="add new recording")

@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into user (username,email,password,sex,photo,country_id) values (:username,:email,:password,:sex,:photo,:country_id)",request.form)
        user = query_db('select * from user')
        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")
    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")

@app.route("/add_one_photos", methods=["GET","POST"])
def add_one_photos():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into photos (name,pic,author_id) values (:name,:pic,:author_id)",request.form)
        user = query_db('select * from photos')
        return render_template("photosform.html", photoss=user, one_user=one_user, the_title="add new photos")
    user = query_db('select * from photos')
    one_user = query_db("select * from photos limit 1", one=True)
    return render_template("photosform.html", photoss=user, one_user=one_user, the_title="add new photos")

@app.route("/add_one_video", methods=["GET","POST"])
def add_one_video():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into video (name,vid,author_id) values (:name,:vid,:author_id)",request.form)
        user = query_db('select * from video')
        return render_template("videoform.html", videos=user, one_user=one_user, the_title="add new video")
    user = query_db('select * from video')
    one_user = query_db("select * from video limit 1", one=True)
    return render_template("videoform.html", videos=user, one_user=one_user, the_title="add new video")

@app.route("/add_one_post", methods=["GET","POST"])
def add_one_post():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into post (title,content,author_id) values (:title,:content,:author_id)",request.form)
        user = query_db('select * from post')
        return render_template("postform.html", posts=user, one_user=one_user, the_title="add new post")
    user = query_db('select * from post')
    one_user = query_db("select * from post limit 1", one=True)
    return render_template("postform.html", posts=user, one_user=one_user, the_title="add new post")

@app.route("/add_one_recording", methods=["GET","POST"])
def add_one_recording():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into recording (title,rec,author_id) values (:title,:rec,:author_id)",request.form)
        user = query_db('select * from recording')
        return render_template("recordingform.html", recordings=user, one_user=one_user, the_title="add new recording")
    user = query_db('select * from recording')
    one_user = query_db("select * from recording limit 1", one=True)
    return render_template("recordingform.html", recordings=user, one_user=one_user, the_title="add new recording")

@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into user (username,email,password,sex,photo,country_id) values (:username,:email,:password,:sex,:photo,:country_id)",request.form)
        user = query_db('select * from user')
        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")
    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")

@app.route("/add_one_photos", methods=["GET","POST"])
def add_one_photos():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into photos (name,pic,author_id) values (:name,:pic,:author_id)",request.form)
        user = query_db('select * from photos')
        return render_template("photosform.html", photoss=user, one_user=one_user, the_title="add new photos")
    user = query_db('select * from photos')
    one_user = query_db("select * from photos limit 1", one=True)
    return render_template("photosform.html", photoss=user, one_user=one_user, the_title="add new photos")

@app.route("/add_one_video", methods=["GET","POST"])
def add_one_video():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into video (name,vid,author_id) values (:name,:vid,:author_id)",request.form)
        user = query_db('select * from video')
        return render_template("videoform.html", videos=user, one_user=one_user, the_title="add new video")
    user = query_db('select * from video')
    one_user = query_db("select * from video limit 1", one=True)
    return render_template("videoform.html", videos=user, one_user=one_user, the_title="add new video")

@app.route("/add_one_post", methods=["GET","POST"])
def add_one_post():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into post (title,content,author_id) values (:title,:content,:author_id)",request.form)
        user = query_db('select * from post')
        return render_template("postform.html", posts=user, one_user=one_user, the_title="add new post")
    user = query_db('select * from post')
    one_user = query_db("select * from post limit 1", one=True)
    return render_template("postform.html", posts=user, one_user=one_user, the_title="add new post")

@app.route("/add_one_recording", methods=["GET","POST"])
def add_one_recording():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into recording (title,rec,author_id) values (:title,:rec,:author_id)",request.form)
        user = query_db('select * from recording')
        return render_template("recordingform.html", recordings=user, one_user=one_user, the_title="add new recording")
    user = query_db('select * from recording')
    one_user = query_db("select * from recording limit 1", one=True)
    return render_template("recordingform.html", recordings=user, one_user=one_user, the_title="add new recording")

@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into user (username,email,password,sex,photo,country_id) values (:username,:email,:password,:sex,:photo,:country_id)",request.form)
        user = query_db('select * from user')
        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")
    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")

@app.route("/add_one_photos", methods=["GET","POST"])
def add_one_photos():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into photos (name,pic,author_id) values (:name,:pic,:author_id)",request.form)
        user = query_db('select * from photos')
        return render_template("photosform.html", photoss=user, one_user=one_user, the_title="add new photos")
    user = query_db('select * from photos')
    one_user = query_db("select * from photos limit 1", one=True)
    return render_template("photosform.html", photoss=user, one_user=one_user, the_title="add new photos")

@app.route("/add_one_video", methods=["GET","POST"])
def add_one_video():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into video (name,vid,author_id) values (:name,:vid,:author_id)",request.form)
        user = query_db('select * from video')
        return render_template("videoform.html", videos=user, one_user=one_user, the_title="add new video")
    user = query_db('select * from video')
    one_user = query_db("select * from video limit 1", one=True)
    return render_template("videoform.html", videos=user, one_user=one_user, the_title="add new video")

@app.route("/add_one_post", methods=["GET","POST"])
def add_one_post():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into post (title,content,author_id) values (:title,:content,:author_id)",request.form)
        user = query_db('select * from post')
        return render_template("postform.html", posts=user, one_user=one_user, the_title="add new post")
    user = query_db('select * from post')
    one_user = query_db("select * from post limit 1", one=True)
    return render_template("postform.html", posts=user, one_user=one_user, the_title="add new post")

@app.route("/add_one_recording", methods=["GET","POST"])
def add_one_recording():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into recording (title,rec,author_id) values (:title,:rec,:author_id)",request.form)
        user = query_db('select * from recording')
        return render_template("recordingform.html", recordings=user, one_user=one_user, the_title="add new recording")
    user = query_db('select * from recording')
    one_user = query_db("select * from recording limit 1", one=True)
    return render_template("recordingform.html", recordings=user, one_user=one_user, the_title="add new recording")

@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into user (username,email,password,sex,photo,country_id) values (:username,:email,:password,:sex,:photo,:country_id)",request.form)
        user = query_db('select * from user')
        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")
    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")

