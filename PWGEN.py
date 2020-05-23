from random import randint
from time import strftime
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, IntegerField
from random import  *
import string

value = string.ascii_letters + string.punctuation + string.digits + string.ascii_lowercase + string.ascii_uppercase


DEBUG = True
app = Flask(__name__)
app = Flask(__name__, template_folder='../templates')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'

class ReusableForm(Form):
    website = TextField('website:', validators=[validators.data_required()])
    username = TextField('username:', validators=[validators.data_required()])
    pwlen = IntegerField('pwlen:', validators=[validators.data_required()])


@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)


    if request.method == 'POST':
        website=request.form['website']
        username=request.form['username']
        email=request.form['email']
        pwlen=request.form['pwlen']
        res = int(pwlen)
        y = "".join(choice(value) for x in range(res))
    if form.validate():
            flash('Your password for {}, with username: {}, has the following password - {}'.format(website, username, y ))

    else:
            flash('Error: All Fields are Required')

    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()