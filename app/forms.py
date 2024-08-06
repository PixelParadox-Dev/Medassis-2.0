from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,RadioField,IntegerField,SelectField,DecimalField,SelectMultipleField
from wtforms.validators import Length, Email, DataRequired, ValidationError

class DiabetesForm(FlaskForm):

    username=StringField('Name',validators=[DataRequired(),Length(max=100)])
    gender=RadioField('Gender',validators=[DataRequired()],choices=['Male','Female','Others'])
    age=IntegerField('Age',validators=[DataRequired()])
    address=StringField('Address',validators=[DataRequired(),Length(max=250)])
    pincode=IntegerField('Pincode',validators=[DataRequired()])
    hypertension=RadioField('Hypertension',validators=[DataRequired()],choices=['Yes','No'])
    previousHeartDisease=RadioField('Previous Heart Disease',validators=[DataRequired()],choices=['Yes','No'])
    smoking_History=SelectField("Smoking History",validators=[DataRequired()],choices=[('never','Never'),('former','Former'),('current','Current'),('notcurrent','Not Current'),('ever','Ever'),('other','Other')])
    weight=DecimalField("Weight (in kg)",validators=[DataRequired()],places=2)
    height=DecimalField("Height (in m)",validators=[DataRequired()],places=2)
    hba1clvl=SelectField("HbA1c Level",validate_choice=[DataRequired()],choices=[('3below','below 3'),('34','3-4'),('45','4-5'),('56','5-6'),('67','6-7'),('78','7-8'),('89','8-9'),('9above','above 9')])
    blood_glucose=IntegerField('Blood Glucose Level',validators=[DataRequired()])
    # email=StringField('Email',validators=[DataRequired(),Email(),Length(max=50)])
    phone=IntegerField('Phone Number',validators=[DataRequired()])
    submit=SubmitField('Submit')

class LiverForm(FlaskForm):
    username=StringField('Name',validators=[DataRequired(),Length(max=100)])
    age=IntegerField('Age',validators=[DataRequired()])
    gender=RadioField('Gender',validators=[DataRequired()],choices=['Male','Female','Others'])
    address=StringField('Address',validators=[DataRequired(),Length(max=250)])
    pincode=IntegerField('Pincode',validators=[DataRequired()])
    total_protein=DecimalField('Total Proteins (g/dL)',validators=[DataRequired()],places=2)
    albumin=DecimalField('Albumin (g/dL)',validators=[DataRequired()],places=2)
    ag_ratio=DecimalField('A/G Ratio',validators=[DataRequired()],places=2)
    total_bilirubin=DecimalField('Total Bilirubin (mg/dl)',validators=[DataRequired()],places=2)
    direct_bilirubin=DecimalField('Direct Bilirubin (mg/dl)',validators=[DataRequired()],places=2)
    alkaline_phosphate=IntegerField('Alkaline Phosphate (IU/L)',validators=[DataRequired()])
    sgpt=IntegerField('SGPT (U/L)',validators=[DataRequired()])
    sgot=IntegerField('SGOT (U/L)',validators=[DataRequired()])
    height=DecimalField("Height (in m)",validators=[DataRequired()],places=2)
    weight=DecimalField("Weight (in kg)",validators=[DataRequired()],places=2)
    phone=IntegerField('Phone Number',validators=[DataRequired()])
    submit=SubmitField('Submit')

class KidneyForm(FlaskForm):
    username=StringField('Name',validators=[DataRequired(),Length(max=100)])
    gender=RadioField('Gender',validators=[DataRequired()],choices=['Male','Female','Others'])
    height=DecimalField("Height (in m)",validators=[DataRequired()],places=2)
    weight=DecimalField("Weight (in kg)",validators=[DataRequired()],places=2)
    smoke_alco=RadioField('Smoking and Alcohol History',validators=[DataRequired()],choices=['Smoking','Alcohol','Both','None'])
    age=IntegerField('Age',validators=[DataRequired()])
    physical_activity=IntegerField('Physical Activity (Weekly)',validators=[DataRequired()])
    kidney_diet_score=IntegerField('Kidney Diet Score (0-10)',validators=[DataRequired()])
    genetics=SelectMultipleField('Genetics',validate_choice=[DataRequired()],choices=[('diasease','Family History Diasease'),('hypertension','Family History Hypertension'),('diabetes','Family History Diabetes')])
    urinary_tract=RadioField('Urinary Tract Infections',validators=[DataRequired()],choices=['Yes','No'])
    systoyic_bp=IntegerField('Systoyic BP(mmHg)',validators=[DataRequired()])
    diastotic_bp=IntegerField('Diastotic BP(mmHg)',validators=[DataRequired()])
    fasting_blood_sugar=DecimalField('Fasting Blood Sugar',validators=[DataRequired()],places=2)
    hba1clvl=DecimalField("HbA1c Level",validators=[DataRequired()],places=2)
    serum_creative=DecimalField('Serum Creative(mg/dL)',validators=[DataRequired()],places=2)
    bunlvl=DecimalField('BUN Level',validators=[DataRequired()],places=2)
    gfr=DecimalField('GFR (ml/min/1.73m^2)',validators=[DataRequired()],places=2)
    protein_in_urine=DecimalField('Protein in Urine(g/day)',validators=[DataRequired()],places=2)
    serum_electrolyes_sodium=DecimalField('Serum Electrolytes Sodium(mEq/L)',validators=[DataRequired()],places=2)
    serum_electrolyes_potassium=DecimalField('Serum Electrolytes Potassium(mEq/L)',validators=[DataRequired()],places=2)
    haemoglobin_lvl=DecimalField('Haemoglobin Level(g/dL)',validators=[DataRequired()],places=2)
    cholestrol_lvl=DecimalField('Cholestrol Level(mg/dL)',validators=[DataRequired()],places=2)
    diuretics=RadioField('Diuretics',validators=[DataRequired()],choices=['Yes','No'])
    edema=RadioField('Edema',validators=[DataRequired()],choices=['Yes','No'])
    muscle=SelectField('Muscle cramps',validators=[DataRequired()],choices=[('low','Low'),('moderate','Moderate'),('high','High')])
    itching=SelectField('Itching score',validators=[DataRequired()],choices=[('low','Low'),('moderate','Moderate'),('high','High')])
    submit=SubmitField('Submit')



class SignUpForm(FlaskForm):
    username=StringField('Name',validators=[DataRequired(),Length(max=100)])
    email=StringField('Email',validators=[DataRequired(),Email(),Length(max=50)])
    password=PasswordField('Password',validators=[DataRequired(),Length(max=6)])
    submit=SubmitField('Sign Up')

class SignInForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email(),Length(max=50)])
    password=PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Login')

class OtpForm(FlaskForm):
    otp=IntegerField('OTP',validators=[DataRequired(),Length(max=6)])
    submit=SubmitField('Verify')