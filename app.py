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

  if request.method == "POST":

    if request.form.get('pub/priv') == "private":
      blood = request.form['blood']
      weight = request.form['weight']
      illness = request.form['illness']
      age = request.form['age']
      height = request.form['height']
      timeinhos = request.form['timeinhos']
      gender = request.form.get('gender')
      medicine = request.form['medicine']
      hospital = request.form['hospital']
      doctor = request.form['doctor']
      anesthesiatypes = []
      if 'general' in request.form:
        anesthesiatypes.append(request.form['general'])
      if 'regional' in request.form:
        anesthesiatypes.append(request.form['regional'])
      if 'sedation' in request.form:
        anesthesiatypes.append(request.form['sedation'])
      if 'local' in request.form:
        anesthesiatypes.append(request.form['local'])

      treatmenttype = []
      if 'surgery' in request.form:
        treatmenttype.append(request.form['surgery'])
      if 'medicinee' in request.form:
        treatmenttype.append(request.form['medicinee'])
      if 'physotherapy' in request.form:
        treatmenttype.append(request.form['physotherapy'])
      if 'hydro' in request.form:
        treatmenttype.append(request.form['hydro'])
      if 'therapy' in request.form:
        treatmenttype.append(request.form['therapy'])
      if 'chemotherapy' in request.form:
        treatmenttype.append(request.form['chemotherapy'])
      if 'radiation' in request.form:
        treatmenttype.append(request.form['radiation'])
      if 'biological' in request.form:
        treatmenttype.append(request.form['biological'])
      if 'hormonal' in request.form:
        treatmenttype.append(request.form['hormonal'])
      if 'targeted' in request.form:
        treatmenttype.append(request.form['targeted'])


      symptomsafter = []
      if 'onee' in request.form:
        symptomsafter.append(request.form['onee'])
      if 'twoe' in request.form:
        symptomsafter.append(request.form['twoe'])
      if 'threee' in request.form:
        symptomsafter.append(request.form['threee'])
      if 'foure' in request.form:
        symptomsafter.append(request.form['foure'])
      if 'fivee' in request.form:
        symptomsafter.append(request.form['fivee'])
      if 'sixe' in request.form:
        symptomsafter.append(request.form['sixe'])
      if 'sevene' in request.form:
        symptomsafter.append(request.form['sevene'])
      if 'eighte' in request.form:
        symptomsafter.append(request.form['eighte'])
      if 'ninee' in request.form:
        symptomsafter.append(request.form['ninee'])
      if 'tene' in request.form:
        symptomsafter.append(request.form['tene'])
      if 'elevene' in request.form:
        symptomsafter.append(request.form['elevene'])
      if 'twelvee' in request.form:
        symptomsafter.append(request.form['twelvee'])
      if 'thirteene' in request.form:
        symptomsafter.append(request.form['thirteene'])
      if 'fourteene' in request.form:
        symptomsafter.append(request.form['fourteene'])

      symptomsbefore = []
      if 'one' in request.form:
        symptomsbefore.append(request.form['one'])
      if 'two' in request.form:
        symptomsbefore.append(request.form['two'])
      if 'three' in request.form:
        symptomsbefore.append(request.form['three'])
      if 'four' in request.form:
        symptomsbefore.append(request.form['four'])
      if 'five' in request.form:
        symptomsbefore.append(request.form['five'])
      if 'six' in request.form:
        symptomsbefore.append(request.form['six'])
      if 'seven' in request.form:
        symptomsbefore.append(request.form['seven'])
      if 'eight' in request.form:
        symptomsbefore.append(request.form['eight'])
      if 'nine' in request.form:
        symptomsbefore.append(request.form['nine'])
      if 'ten' in request.form:
        symptomsbefore.append(request.form['ten'])
      if 'eleven' in request.form:
        symptomsbefore.append(request.form['eleven'])
      if 'twelve' in request.form:
        symptomsbefore.append(request.form['twelve'])
      if 'thirteen' in request.form:
        symptomsbefore.append(request.form['thirteen'])
      if 'fourteen' in request.form:
        symptomsbefore.append(request.form['fourteen'])

      notes = request.form["notes"]
      cost = request.form["cost"]

      Info = {"age":age, "height":height, "gender": gender, "blood":blood, "specifics":{"illness":illness, "timeinhos":timeinhos, "medicine":medicine, "symptomsbefore":symptomsbefore, "symptomsafter":symptomsafter, "treatmenttype":treatmenttype, "anesthesiatypes":anesthesiatypes, "Doctor's Notes":notes, "Total Cost":cost}}
      db.child("Private").child(hospital).child("Treatments").push(Info)
      return redirect(url_for("login"))

    if request.form.get('pub/priv') == "public":
      blood = request.form['blood']
      weight = request.form['weight']
      illness = request.form['illness']
      age = request.form['age']
      height = request.form['height']
      timeinhos = request.form['timeinhos']
      gender = request.form.get('gender')
      medicine = request.form['medicine']
      hospital = request.form['hospital']
      doctor = request.form['doctor']
      anesthesiatypes = []
      if 'general' in request.form:
        anesthesiatypes.append(request.form['general'])
      if 'regional' in request.form:
        anesthesiatypes.append(request.form['regional'])
      if 'sedation' in request.form:
        anesthesiatypes.append(request.form['sedation'])
      if 'local' in request.form:
        anesthesiatypes.append(request.form['local'])

      treatmenttype = []
      if 'surgery' in request.form:
        treatmenttype.append(request.form['surgery'])
      if 'medicinee' in request.form:
        treatmenttype.append(request.form['medicinee'])
      if 'physotherapy' in request.form:
        treatmenttype.append(request.form['physotherapy'])
      if 'hydro' in request.form:
        treatmenttype.append(request.form['hydro'])
      if 'therapy' in request.form:
        treatmenttype.append(request.form['therapy'])
      if 'chemotherapy' in request.form:
        treatmenttype.append(request.form['chemotherapy'])
      if 'radiation' in request.form:
        treatmenttype.append(request.form['radiation'])
      if 'biological' in request.form:
        treatmenttype.append(request.form['biological'])
      if 'hormonal' in request.form:
        treatmenttype.append(request.form['hormonal'])
      if 'targeted' in request.form:
        treatmenttype.append(request.form['targeted'])


      symptomsafter = []
      if 'onee' in request.form:
        symptomsafter.append(request.form['onee'])
      if 'twoe' in request.form:
        symptomsafter.append(request.form['twoe'])
      if 'threee' in request.form:
        symptomsafter.append(request.form['threee'])
      if 'foure' in request.form:
        symptomsafter.append(request.form['foure'])
      if 'fivee' in request.form:
        symptomsafter.append(request.form['fivee'])
      if 'sixe' in request.form:
        symptomsafter.append(request.form['sixe'])
      if 'sevene' in request.form:
        symptomsafter.append(request.form['sevene'])
      if 'eighte' in request.form:
        symptomsafter.append(request.form['eighte'])
      if 'ninee' in request.form:
        symptomsafter.append(request.form['ninee'])
      if 'tene' in request.form:
        symptomsafter.append(request.form['tene'])
      if 'elevene' in request.form:
        symptomsafter.append(request.form['elevene'])
      if 'twelvee' in request.form:
        symptomsafter.append(request.form['twelvee'])
      if 'thirteene' in request.form:
        symptomsafter.append(request.form['thirteene'])
      if 'fourteene' in request.form:
        symptomsafter.append(request.form['fourteene'])

      symptomsbefore = []
      if 'one' in request.form:
        symptomsbefore.append(request.form['one'])
      if 'two' in request.form:
        symptomsbefore.append(request.form['two'])
      if 'three' in request.form:
        symptomsbefore.append(request.form['three'])
      if 'four' in request.form:
        symptomsbefore.append(request.form['four'])
      if 'five' in request.form:
        symptomsbefore.append(request.form['five'])
      if 'six' in request.form:
        symptomsbefore.append(request.form['six'])
      if 'seven' in request.form:
        symptomsbefore.append(request.form['seven'])
      if 'eight' in request.form:
        symptomsbefore.append(request.form['eight'])
      if 'nine' in request.form:
        symptomsbefore.append(request.form['nine'])
      if 'ten' in request.form:
        symptomsbefore.append(request.form['ten'])
      if 'eleven' in request.form:
        symptomsbefore.append(request.form['eleven'])
      if 'twelve' in request.form:
        symptomsbefore.append(request.form['twelve'])
      if 'thirteen' in request.form:
        symptomsbefore.append(request.form['thirteen'])
      if 'fourteen' in request.form:
        symptomsbefore.append(request.form['fourteen'])

      notes = request.form["notes"]
      cost = request.form["cost"]

      Info = {"age":age, "height":height, "gender": gender, "blood":blood, "specifics":{"illness":illness, "timeinhos":timeinhos, "medicine":medicine, "symptomsbefore":symptomsbefore, "symptomsafter":symptomsafter, "treatmenttype":treatmenttype, "anesthesiatypes":anesthesiatypes, "Doctor's Notes":notes, "Total Cost":cost}}
      db.child("Public").child(hospital).child("Treatments").push(Info)
      return redirect(url_for('login'))


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