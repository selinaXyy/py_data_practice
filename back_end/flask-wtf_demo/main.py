from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_babel import _
from wtforms import StringField, PasswordField, SubmitField, validators, Form
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.secret_key = "this-is-the-secret-key"

class LoginForm(FlaskForm):
    #needs to install 'email_validator'
    email = StringField(label='Email', validators=[
        validators.Length(min=6, message=_('Please make sure you entered a valid email address.')), 
        validators.Email(message=_('Invalid email address.'))])
    password = PasswordField(label='Password', validators=[validators.length(min=8, message=_('Password must be at least 8 characters.'))])
    submit = SubmitField(label="Login")
    csrf_token = app.secret_key

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_email = form.email.data
        user_password = form.password.data
        print(user_email, user_password)
        return render_template('success.html')
    else: #if validation errors happened during form submission
        return render_template('login.html', form=form)
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
