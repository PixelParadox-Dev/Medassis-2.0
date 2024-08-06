from app import app
from flask import render_template
from app.forms import DiabetesForm,OtpForm,SignInForm,SignUpForm,LiverForm,KidneyForm

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

@app.route('/sign-in')
def signin():
    signinform=SignInForm()
    if signinform.validate_on_submit():
        email=signinform.username.data
        password=signinform.password.data

    return render_template('signin.html',signin=signinform)

@app.route('/sign-up')
def signup():
    signupform=SignUpForm()
    if signupform.validate_on_submit():
        username=signupform.username.data
        email=signupform.email.data
        password=signupform.password.data

    return render_template('signup.html',signup=signupform)

@app.route('/otp')
def otp():
    otpform=OtpForm()
    if otpform.validate_on_submit():
        otp=otpform.otp.data

    return render_template('otp.html',otpform=otpform)

@app.route('/diabetes-form')
def diabetes():
    diabetesform=DiabetesForm()
    if diabetesform.validate_on_submit():
        username=diabetesform.username.data
        gender=diabetesform.gender.data
        age=diabetesform.age.data
        address=diabetesform.address.data

        pincode = diabetesform.pincode.data
        hypertension = diabetesform.hypertension.data
        previousHeartDisease = diabetesform.previousHeartDisease.data
        smoking_History = diabetesform.smoking_History.data
        weight = diabetesform.weight.data
        height = diabetesform.height.data
        hba1clvl = diabetesform.hba1clvl.data
        blood_glucose = diabetesform.blood_glucose.data
        email = diabetesform.email.data
        phone = diabetesform.phone.data
    return render_template('diabetesform.html',form=diabetesform)

@app.route('/liver-form')
def liver():
    liverform=LiverForm()
    if liverform.validate_on_submit():
        username = liverform.username.data
        age = liverform.age.data
        gender = liverform.gender.data
        address = liverform.address.data
        pincode = liverform.pincode.data
        total_protein = liverform.total_protein.data
        albumin = liverform.albumin.data
        ag_ratio = liverform.ag_ratio.data
        total_bilirubin = liverform.total_bilirubin.data
        direct_bilirubin = liverform.direct_bilirubin.data
        alkaline_phosphate = liverform.alkaline_phosphate.data
        sgpt = liverform.sgpt.data
        sgot = liverform.sgot.data
        height = liverform.height.data
        weight = liverform.weight.data
        phone = liverform.phone.data
        
    
    return render_template('liver.html',liverform=liverform)

@app.route('/kidney-form')
def kidney():
    kidneyform=KidneyForm()
    if kidneyform.validate_on_submit():
        username = kidneyform.username.data
        gender = kidneyform.gender.data
        height = kidneyform.height.data
        weight = kidneyform.weight.data
        smoke_alco = kidneyform.smoke_alco.data
        age = kidneyform.age.data
        physical_activity = kidneyform.physical_activity.data
        kidney_diet_score = kidneyform.kidney_diet_score.data
        genetics = kidneyform.genetics.data
        urinary_tract = kidneyform.urinary_tract.data
        systoyic_bp = kidneyform.systoyic_bp.data
        diastotic_bp = kidneyform.diastotic_bp.data
        fasting_blood_sugar = kidneyform.fasting_blood_sugar.data
        hba1clvl = kidneyform.hba1clvl.data
        serum_creative = kidneyform.serum_creative.data
        bunlvl = kidneyform.bunlvl.data
        gfr = kidneyform.gfr.data
        protein_in_urine = kidneyform.protein_in_urine.data
        serum_electrolyes_sodium = kidneyform.serum_electrolyes_sodium.data
        serum_electrolyes_potassium = kidneyform.serum_electrolyes_potassium.data
        haemoglobin_lvl = kidneyform.haemoglobin_lvl.data
        cholestrol_lvl = kidneyform.cholestrol_lvl.data
        diuretics = kidneyform.diuretics.data
        edema = kidneyform.edema.data
        muscle = kidneyform.muscle.data
        itching = kidneyform.itching.data
        

    return render_template('kidney.html',kidneyform=kidneyform)
