import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()


 #Create the table for the csv data of the office lines(if not exists)
mycursor.execute(""" CREATE TABLE IF NOT EXISTS THEOFFICE.CITAZIONI (
    id_puntata INTEGER PRIMARY KEY,
    Personaggio VARCHAR (30),
    Citazione VARCHAR(300),
    Stagione INTEGER,
    Numero_episodio INTEGER
    
  )""")

#Delete data from the table Clsh_Unit
mycursor.execute("DELETE FROM THEOFFICE.CITAZIONI")
mydb.commit()

#Read data from a csv file
clash_data = pd.read_csv('./Citazioni.csv', index_col=False, delimiter = ',')
clash_data = clash_data.fillna('Null')
print(clash_data.head(20))

#Fill the table
for i,row in clash_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO THEOFFICE.CITAZIONI (id_puntata,Personaggio,Citazione,Stagione,Numero_episodio ) VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM THEOFFICE.CITAZIONI")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)