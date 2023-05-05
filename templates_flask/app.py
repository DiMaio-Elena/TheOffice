from flask import render_template
from flask import Flask

import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="THEOFFICE"
)

mycursor=mydb.cursor()
@app.route ('/')
def unitList():
    mycursor.execute("SELECT * FROM EPISODES")
    myresult = mycursor.fetchall()
    return render_template('episodes.html', units=myresult)