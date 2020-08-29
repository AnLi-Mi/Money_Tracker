from flask import Flask, render_template, request

from flaskext.mysql import MySQL

#initialising flask app
app=Flask(__name__)

#initialising and configuring MySQL DB
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
        #turning user's posts into variables 
        pur_date=request.form.get('pur_date')
        amount=request.form.get('amount')
        category=request.form.get('category')
        notes=request.form.get('notes')
        for_whom=request.form.get('for')
        who_paid=request.form.get('who_paid')
        #preparing a string for a SQL qeuery inserting values posted by the user
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
    spendings = ''
    query = 'SELECT * FROM money_track.spendings'
    spendings = display_spendings(query)
    return render_template('seealltransactions.html', spendings=spendings)

@app.route('/monthlysummary', methods=['GET', 'POST'])
def monthly_summary():
    summed_spendings = ''
    category = ''
    if request.method == "POST" and "chosen_category" in request.form:
        category=request.form.get("chosen_category")
        query = f"SELECT SUM(amount) FROM money_track.spendings WHERE category = '{category}';"
        summed_spendings = display_spendings(query)
    return render_template('monthlysummary.html', summed_spendings=summed_spendings, category=category)



#checking connection
def connect_msql():
    conn = mysql.connect()
    if (conn):
    # Carry out normal procedure
        print ("Connection successful")
    else:
    # Terminate
        print ("Connection unsuccessful")

connect_msql()

# function for insert SQL query
def insert_query(query):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

#function displaying records
def display_spendings(query):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(query)
    result=cursor.fetchall()
    return result













