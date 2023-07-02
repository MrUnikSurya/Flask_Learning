from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/coding_flask'
db = SQLAlchemy(app)

class Contacts(db.Model):
    # srno, Name, email, phone_num, mes, date
    srno = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String(80), unique=False, nullable = False)
    email = db.Column(db.String(20), unique = True, nullable=False)
    phone_num = db.Column(db.String(12), unique=True, nullable=False)
    mes = db.Column(db.String(120), unique=False, nullable=False)
    date = db.Column(db.String(12), unique=False)

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/about")
def about():
    return render_template('about.html')
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        # Add entry to the database
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        msg = request.form.get("msg")

        entry = Contacts(Name=name, email=email, phone_num=phone, mes=msg, date=datetime.now())
        db.session.add(entry)
        db.session.commit()

    return render_template('contact.html')
@app.route("/post")
def post():
    return render_template('post.html')

app.run(debug=True)