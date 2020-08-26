from flask import Flask, render_template

from flaskext.mysql import MySQL

app=Flask(__name__)
mysql=MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '8G13rm3k'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/addtransaction')
def add_transaction():
    return render_template('addtransaction.html')

@app.route('/seealltransactions')
def see_all():
    return render_template('seealltransactions.html')

@app.route('/monthlysummary')
def monthly_summary():
    return render_template('monthlysummary.html')


def connect_msql():
    conn = mysql.connect()
    if (conn):
    # Carry out normal procedure
        print ("Connection successful")
    else:
    # Terminate
        print ("Connection unsuccessful")


connect_msql()




