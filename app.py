from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import connect as c

client = ""
app = Flask(__name__)

#1. Configuration of SQLite for sqlalchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////test.db"
app.app_context()
db = SQLAlchemy(app)

#2. Now create class to create table and its column 
# class signup(db.Model) :
#     #sno is a primary key
#     sno = db.Column(db.Integer, primary_key=True)
#     fullname= db.Column(db.String(200),nullable=False)
#     email = db.Column(db.String(200),nullable=False)
#     message = db.Column(db.String(500),nullable = False)
#     #date_created = db.Column(db.Datetime, default=datetime.utcnow)

#     def __repr__(self) -> str:
#         return f"{self.sno} - {self.email} - {self.fullname} - {self.message}"

@app.route('/')
def hello_world():
     return render_template('index.html') 

# @app.route('/signup')
# def signup():
#     return 'Hello, Welcome this is signup page!'

# @app.route('/signup')
# def contactus():
#     return render_template('index.html') 

@app.route('/render', methods=['GET','POST'])
def render():
    if request.method=="POST":
        print("Inside POST method")
        fullname=request.form['fullname']
        email= request.form['email']
        message = request.form['message']

        db = client.get_database("FirstMongoDb")
        collection = db.ContactUs
        # db = client["FirstMongoDb"]
        # collection = db["ContactUs"]
        print("After Contact us Db")

        dictionary = {"Full Name" : fullname, "Email" : email, "Message" : message}
         #You have to create one dictionary for mat object and insert one row then only you can see table on mongoDb compass
        collection.insert_one(dictionary)
        print("Inserted Dictionory successfully")
    return render_template('thankyou.html')  

# @app.route('/thankyou', methods=['GET','POST'])
# def thankyou():
#     return render_template('thankyou.html')  


if __name__ == "__main__":
    #client = c.connectdb()
    client = c.connectatlasdb()
    print("Return after Connection")
    app.run(debug=True,port=8000)