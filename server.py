from flask import Flask, render_template, redirect, flash, request
import re
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key="bBBbbbbbbbBBBiiiLLLLLll"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register',methods=['POST'])
def register():
    #EMAIL VALIDATION:
    if len(request.form['email']) < 1:
        flash("Email cannot be empty!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email must be valid!")
    
    #FIRST NAME VALIDATION:
    if len(request.form['first_name']) < 1:
        flash("First name cannot be empty!")
    elif not (request.form['first_name']).isalpha():
        flash("First name can only contain letters!")
    
    #LAST NAME VALIDATION:
    if len(request.form['last_name']) < 1:
        flash("Last name cannot be empty!")
    elif not (request.form['last_name']).isalpha():
        flash("Last name can only contain letters!")
    
    #PASSWORD VALIDATION:
    if len(request.form['password']) < 1:
        flash("Password cannot be empty!")
    elif len(request.form['password']) < 8:
        flash("Password is too short!")
    elif not (any(x.isupper() for x in request.form['password'])):
        flash("Password must contain at least one capital letter")
    elif not (any(x.isdigit() for x in request.form['password'])):
        flash("Password must contain at least one digit")
    
    #CONFIRM VALIDATION:
    if len(request.form['confirm']) < 1:
        flash("Field cannot be empty!")
    elif request.form['confirm'] != request.form['password']:
        flash("Password and Confirmation MUST match!")

    #BIRTHDAY VALIDATION:
    correctDate = None
    try: 
        birthday = datetime.datetime(int(request.form['year']),int(request.form['month']),int(request.form['date']))
        correctDate=True
    except ValueError:
        correctDate = False
    if not correctDate:
        flash("Please enter a valid birthday")

    flash("Thanks for submitting your info")

    return redirect('/')

app.run(debug = True)
