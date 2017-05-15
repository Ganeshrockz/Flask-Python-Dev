from flask import Flask, flash, render_template, redirect, url_for
from flask.ext.pymongo import PyMongo
from flask import request
app=Flask(__name__)
app.config['MONGO_DBNAME']='stud'
app.config['MONGO_URI']='mongodb://localhost:27017/stud'
mongo=PyMongo(app)
"""
@app.route('/add')
def add():
    user=mongo.db.users
    user.insert({"name":"Ganesh","age":19})
    return "Added"

@app.route('/find')
def find():
    user=mongo.db.users
    data=user.find_one({"name":"Ganesh"})
    return data["name"]
    """
@app.route('/',methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        name=request.form['name']
        passw=request.form['password']
        if name=="admin123" and passw=="12345":
            return redirect(url_for('display'))
        else:
            return render_template("dashboard.html",err="Login Failed")
    else:
        return render_template("dashboard.html")

@app.route('/form',methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
                user=mongo.db.student
                rollno=request.form['rollno']
                name=request.form['name']
                address=request.form['address']
                year=request.form['year']
                skills=request.form['skills']
                phone=request.form['phone']
                email=request.form['emailid']
                user.insert({"Rollnumber":rollno,"StudentName":name,"Address":address,"Year":year,"Skills":skills,"PhoneNumber":phone,"EmailId":email})
                return redirect(url_for('dashboard'))
    else:
        return render_template("form.html")

@app.route('/display',methods=['GET', 'POST'])
def display():
    data=mongo.db.student
    record=[]
    for rec in data.find():
        record.append({"Rollnumber":rec["Rollnumber"],"StudentName":rec["StudentName"],"Address":rec["Address"],"Year":rec["Year"],"Skills":rec["Skills"],"PhoneNumber":rec["PhoneNumber"],"EmailId":rec["EmailId"]})
        app.logger.info(record)
    return render_template("display.html", studentdata=record)
if __name__ == '__main__':
    app.secret_key = 'ganeshrockz'
    app.run(debug=True)
