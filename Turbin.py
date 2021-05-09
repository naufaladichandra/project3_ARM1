from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL, MySQLdb
import bcrypt
import mysql.connector
import random, datetime, time 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="rafiarma08",
  database="mobiledb"
 
)
mycursor = mydb.cursor()

def Menu():
    print("SIMULATOR MESIN")
    print("1. Data Temperatur pada Inlet dan Outlet")
    print("2. Data Pressure pada Inlet dan Outlet")
    print("3. Data Temperatur & Pressure pada Inlet Outlet")
    print("---------------------")
    print("4. Exit Program")
    print()
    choice = int(input("Enter here: "))

    if(choice==1):
        for i in range(10):
            now = datetime.datetime.now()
            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
            time.sleep(5)
            temperature1 = random.randint(55,65)
            temperature2 = temperature1 + 15
            status = "ON"
            
            mycursor = mydb.cursor()
            mycursor.execute("INSERT INTO temperatur (datetime, status, temperatur_inlet, temperatur_outlet ) VALUES (%s, %s, %s, %s)", (date_time, status, temperature1, temperature2))
        
            mydb.commit()
            print(mycursor.rowcount, "Temperatur Turbin Terdeteksi...")

    if(choice==2):
        for i in range(10):
            now = datetime.datetime.now()
            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
            time.sleep(5)
            pressure1 = random.randint(85,100)
            pressure2 = pressure1 + 15
            status = "GOOD"
            
            mycursor = mydb.cursor()
            mycursor.execute("INSERT INTO pressure (datetime, status, pressure_inlet, pressure_outlet) VALUES (%s, %s, %s, %s, %s, %s)", (date_time, status, pressure1, pressure2))
            mydb.commit()
            print(mycursor.rowcount, "Pressure Turbin ")

    if(choice==3):
        for i in range(10):
            now = datetime.datetime.now()
            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
            time.sleep(2)
            temperature1 = random.randint(50,70)
            temperature2 = temperature1 + 15
            pressure1 = random.randint(85,100)
            pressure2 = pressure1 + 15
            status1 = "ON"
            
            
            mycursor = mydb.cursor()
            mycursor.execute("INSERT INTO monitoring (datetime, status, temperatur_inlet, temperatur_outlet, pressure_inlet, pressure_outlet ) VALUES (%s, %s, %s, %s, %s, %s)", (date_time, status1, temperature1, temperature2, pressure1, pressure2))
           
            mydb.commit()
            print(mycursor.rowcount, "Temperatur & Pressure Turbin ")          

    if(choice==4):
        exit()

Menu()