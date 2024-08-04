from app import app
from flask import render_template
from app.forms import DiabetesForm

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/profile')
def profile():
    return render_template('Profile.html')

@app.route('/community-support')
def community():
    return render_template('community.html')

@app.route('/diabetes-form')
def diabetes():
    myform=DiabetesForm()
    if myform.validate_on_submit():
        # Access form data
        username=myform.username.data
        gender=myform.gender.data
        age=myform.age.data
        address=myform.address.data

        pincode = myform.pincode.data
        hypertension = myform.hypertension.data
        previousHeartDisease = myform.previousHeartDisease.data
        smoking_History = myform.smoking_History.data
        weight = myform.weight.data
        height = myform.height.data
        hba1clvl = myform.hba1clvl.data
        blood_glucose = myform.blood_glucose.data
        email = myform.email.data
        phone = myform.phone.data
    return render_template('diabetesform.html',form=myform)
