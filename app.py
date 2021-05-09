from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL, MySQLdb
import bcrypt 
import mysql.connector
import random, datetime, time 

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rafiarma08'
app.config['MYSQL_DB'] = 'mobiledb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SESSION_TYPE'] = 'filesystem'
mysql = MySQL(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login_user', methods=["GET", "POST"])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')

        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = curl.fetchone()
        curl.close()

        if len(user) > 0:
            if bcrypt.hashpw(password, user["password"].encode('utf-8')) == user["password"].encode('utf-8'):
                session['user'] = user['name']
                session['email'] = user['email']
                return render_template("home.html")
            else:
                return "Error password and email not match"
        else:
            return "Error user not found"
    else:
        return render_template("login_user.html")



@app.route('/login_admin', methods=["GET", "POST"])
def login_admin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')

        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.execute("SELECT * FROM admin WHERE email=%s", (email,))
        admin = curl.fetchone()
        curl.close()

        if len(admin) > 0:
            if bcrypt.hashpw(password, admin["password"].encode('utf-8')) == admin["password"].encode('utf-8'):
                session['admin'] = admin['name']
                session['email'] = admin['email']
                return render_template("home.html")
            else:
                return "Error password and email not match"
        else:
            return "Error admin not found"
    else:
        return render_template("login_admin.html")


@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.clear()
    return render_template("home.html")

@app.route('/register_admin', methods=["GET", "POST"])
def register_admin():
    if request.method == 'GET':
        return render_template("register_admin.html")
    else:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO admin (name, email, password) VALUES (%s,%s,%s)",(name, email, hash_password,))
        mysql.connection.commit()
        session['name'] = request.form['name']
        session['email'] = request.form['email']
        return redirect(url_for('home'))


@app.route('/register_user', methods=["GET", "POST"])
def register_user():
    if request.method == 'GET':
        return render_template("register_user.html")
    else:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email, password) VALUES (%s,%s,%s)",(name, email, hash_password,))
        mysql.connection.commit()
        session['name'] = request.form['name']
        session['email'] = request.form['email']
        return redirect(url_for('home'))

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")


# temperatur user 
@app.route('/monitoring')
def monitoring():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM monitoring")
    rv = cur.fetchall()
    cur.close()
    return render_template('monitoring1.html', monitoring1=rv)

@app.route('/simpan-monitoring', methods=["POST"])
def saveMonitoring():
    datetime = request.form['datetime']
    temperatur = request.form['temperatur']
    pressure = request.form['pressure']
    status = request.form['status']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO monitoring (datetime, temperatur_inlet, temperatur_outlet, pressure_inlet, pressure_outlet, status) VALUES (%s, %s, %s, %s, %s, %s)", (datetime, temperatur_inlet, temperatur_outlet, pressure_inlet, pressure_outlet, status,))
    mysql.connection.commit()
    return redirect(url_for('monitoring1'))


@app.route('/update-monitoring', methods=["POST"])
def updateMonitoring():
    id_data = request.form['id']
    datetime = request.form['datetime']
    temperatur = request.form['temperatur']
    pressure = request.form['pressure']
    status = request.form['status']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE monitoring SET datetime=%s, temperatur_inlet=%s, temperatur_outlet=%s, pressure_inlet=%s, pressure_outlet=%s, status=%s WHERE Id=%s", (datetime, temperatur_inlet, temperatur_outlet, pressure_inlet, pressure_outlet, letstatus, id_data,))
    mysql.connection.commit()
    return redirect(url_for('monitoring1'))

@app.route('/hapus-monitoring/<string:id_data>', methods=["GET"])
def hapusMonitoring(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM monitoring WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('monitoring'))
# end temperatur

# temperatur user 
@app.route('/monitoring2')
def monitoring2():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM monitoring")
    rv = cur.fetchall()
    cur.close()
    return render_template('monitoring2.html', monitoring2=rv)

@app.route('/simpan-monitoring2', methods=["POST"])
def saveMonitoring2():
    datetime = request.form['datetime']
    temperatur = request.form['temperatur']
    pressure = request.form['pressure']
    status = request.form['status']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO monitoring (datetime, temperatur_inlet, temperatur_outlet, pressure_inlet, pressure_outlet, status) VALUES (%s, %s, %s, %s, %s, %s)", (datetime, temperatur_inlet, temperatur_outlet, pressure_inlet, pressure_outlet, status,))
    mysql.connection.commit()
    return redirect(url_for('monitoring2'))


@app.route('/update-monitoring2', methods=["POST"])
def updateMonitoring2():
    id_data = request.form['id']
    datetime = request.form['datetime']
    temperatur = request.form['temperatur']
    pressure = request.form['pressure']
    status = request.form['status']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE monitoring SET datetime=%s, temperatur_inlet=%s, temperatur_outlet=%s, pressure_inlet=%s, pressure_outlet=%s, status=%s WHERE Id=%s", (datetime, temperatur_inlet, temperatur_outlet, pressure_inlet, pressure_outlet, letstatus, id_data,))
    mysql.connection.commit()
    return redirect(url_for('monitoring2'))

@app.route('/hapus-monitoring2/<string:id_data>', methods=["GET"])
def hapusMonitoring2(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM monitoring WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('monitoring'))
# end temperatur


#MONITOR AC FOR USERS


@app.route('/refreshdata', methods=["GET", "POST"])
def refreshdata():
     
        #ini kodingan masukin data
        for i in range(10):
            now = datetime.datetime.now()
            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
            time.sleep(1.5)
            temperature1 = random.randint(50,70)
            temperature2 = temperature1 + 15
            pressure1 = random.randint(85,100)
            pressure2 = pressure1 + 15
            status1 = "ON"
            
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO monitoring (datetime, status, temperatur_inlet, temperatur_outlet, pressure_inlet, pressure_outlet ) VALUES (%s, %s, %s, %s, %s, %s)", (date_time, status1, temperature1, temperature2, pressure1, pressure2))
           
            mysql.connection.commit()
            return redirect(url_for('monitoring2'))


@app.route('/about')
def about():
    return render_template('about.html')  # render a template
   #AKHIR MONITOR AC FOR USERS

#MONITOR
@app.route('/monitoring3')
def monitoring3():
    cur = mysql.connection.cursor()
    cur.execute("SELECT *  FROM monitoring ORDER BY datetime DESC LIMIT 10")
    rv = cur.fetchall()
    cur.close()
    return render_template('monitoring3.html', monitoring=rv)


if __name__ == '__main__':
  
    app.run(debug=True)
