from flask import Flask, request, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader
(template_dir),autoescape=True)

app = Flask(__name__) 
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('home_page.html')

@app.route("/welcome", methods=['POST'])
def welcome(Username):
    Username = request.form['username']
    return render_template('welcome_page.html',name=Username)


@app.route('/', methods=['POST'])
def validate_input():
    username = request.form['username']
    username_error=''
    password = request.form['password']
    password_error=''
    verify = request.form['verify']
    verify_error=''
    email = request.form['email']
    email_error = ''

    if " " in username or len(username) < 3 or len(username)> 20:
        username_error = 'Not a valid username'
        username = ''
    else:
        username = username

    if " " in password:
        password_error = 'Not a valid password'
    if len(password) < 3 or len(password)> 20:
        password_error='Not a valid password'
    if verify != password:
        verify_error="passwords do not match - please re-enter"
    else:
        password = password

    if email != '':
        if " " in email:
            email_error = "Not a valid email address"
            email = ''
        if "@" not in email: 
            email_error = "Not a valid email address - please re-enter"
            email = ''
        if "." not in email:
            email_error = "Not a valid email address - please re-enter"
            email = ''
        if len(email) < 3 or len(email) > 20:
            email_error = "Email must be 3-20 characters long"        
            email = ''
    else:
        email = email   

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome_page.html',name=username)

    else:
        return render_template('home_page.html',username_error=username_error,
            password_error=password_error,verify_error=verify_error,email_error=email_error, 
            username=username,
            password='',
            email=email)

    
app.run()