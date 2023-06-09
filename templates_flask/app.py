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
    mycursor.execute("SELECT * FROM EPISODES,CITAZIONI WHERE id = id_puntata")
    myresult = mycursor.fetchall()
    return render_template('episodes.html', units=myresult)

@app.route ('/Stagione1')
def Stagione1():
    mycursor.execute("SELECT * FROM EPISODES,CITAZIONI WHERE id = id_puntata AND number_of_seasons=1 ")
    myresult1 = mycursor.fetchall()
    return render_template('Stagione1.html', myresult1=myresult1)

@app.route ('/Stagione2')
def Stagione2():
    mycursor.execute("SELECT * FROM EPISODES,CITAZIONI WHERE id = id_puntata AND number_of_seasons=2 ")
    myresult2 = mycursor.fetchall()
    return render_template('Stagione2.html', myresult2=myresult2)
   
 

