from flask import Flask, render_template, request

from flaskext.mysql import MySQL

app=Flask(__name__)
mysql=MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '8G13rm3k'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_DATABASE'] = 'money_track'
mysql.init_app(app)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/addtransaction', methods=['GET', 'POST'])
def add_transaction():
    pur_date=''
    amount=0
    category=''
    notes=''
    for_whom=''
    who_paid=''
    if request.method=='POST' and 'pur_date' in request.form:
        pur_date=request.form.get('pur_date')
        amount=request.form.get('amount')
        category=request.form.get('category')
        notes=request.form.get('notes')
        for_whom=request.form.get('for')
        who_paid=request.form.get('who_paid')
        query=f"INSERT INTO money_track.spendings (purchase_date, amount, category, notes, for_whom, who_paid) VALUES ('{pur_date}', {amount}, '{category}', '{notes}', '{for_whom}', '{who_paid}');"
        insert_query(query)
    return render_template('addtransaction.html',
                           pur_date=pur_date,
                           amount=amount,
                           category=category,
                           notes=notes,
                           for_whom=for_whom,
                           who_paid=who_paid)

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

def insert_query(query):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


connect_msql()






