from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
import timeit
import math

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here

config = {

  "apiKey": "AIzaSyAiUksEus4wyj7k_E5Fq0VujkEb6mc9QpM",

  "authDomain": "casestudies-db4b4.firebaseapp.com",

  "projectId": "casestudies-db4b4",

  "storageBucket": "casestudies-db4b4.appspot.com",

  "messagingSenderId": "950517531298",

  "appId": "1:950517531298:web:b3ccaffe6dcd65ee16cdfb",

  "measurementId": "G-5S7Q1KTLB9",

  "databaseURL": "https://casestudies-db4b4-default-rtdb.europe-west1.firebasedatabase.app"

}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


@app.route('/signup', methods = ["GET", "POST"])
def home():
  error=""
  if request.method == "POST":
    email = request.form["email"]
    password = request.form["password"]
    confpass = request.form["confpassword"]
    fname = request.form["fname"]
    staff = request.form["staff"]
    gender = request.form["gender"]
    did = request.form['id']
    
    try:
      if password == confpass:
        login_session['user'] = auth.create_user_with_email_and_password(email, password)
        user = {"name":fname, "email":email, "password":password,"role":staff, "gender":gender, "id":did}
        db.child("Users").child(login_session['user']['localId']).set(user)
        return redirect(url_for("form"))
    
      else:
        error="*Password do not match!"
        print("*Password do not match!")
    except:
      error = "*Authentication Error!"
      print("*Authentication Error!")

  return render_template('index.html')


@app.route('/form', methods = ["GET", "POST"])
def form():
  return render_template('main.html')

@app.route('/done', methods = ["GET", "POST"])
def done():
  if request.method == "POST":
    patientName =  request.form['patient-name']
    age = request.form['age']
    
  return render_template('done.html')

@app.route('/', methods = ["GET","POST"])
def login():
  error = ""
  if request.method== "POST":
    email = request.form["email"]
    password = request.form["password"]

    try:
      login_session['user'] = auth.sign_in_with_email_and_password(email, password)
      return redirect(url_for("form"))

    except:
      error = "  *Email or Password is Wrong"
  return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)