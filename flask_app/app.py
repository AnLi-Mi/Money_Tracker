from flask import Flask, render_template, request, url_for

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

@app.route('/editrecord', methods=['GET', 'POST'])
def edit():
    current_record = ''
    query_select_record= 'SELECT * FROM money_track.spendings WHERE ID=2'
    current_record = display_spendings(query_select_record)
    new_date=''
    new_amount=''
    new_category=''
    new_note=''
    new_for=''
    new_paid_by =''
    if request.method == "POST" and "new_date" in request.form:
        new_date=request.form.get("new_date")
        new_amount=request.form.get("new_amount")
        new_category=request.form.get("new_category")
        new_note=request.form.get("new_notes")
        new_for=request.form.get("new_for")
        new_paid_by =request.form.get("new_paid_by")
        query=f"UPDATE money_track.spendings SET purchase_date='{new_date}', amount = '{new_amount}', category='{new_category}', notes = '{new_note}', for_whom='{new_for}', who_paid ='{new_paid_by}'  WHERE id=2"
        update_record(query)
    return render_template('editrecord.html', current_record=current_record, new_date=new_date, new_amount=new_amount, new_category=new_category, new_note=new_note, new_for=new_for, new_paid_by=new_paid_by)

@app.route('/monthlysummary', methods=['GET', 'POST'])
def monthly_summary():
    summed_spendings = ''
    category = ''
    for_whom=''
    onclick_test()
    if request.method == "POST" and "chosen_category" in request.form:
        category=request.form.get("chosen_category")
        for_whom=request.form.get("for")
        query = f"SELECT SUM(amount) FROM money_track.spendings WHERE category = '{category}' and for_whom='{for_whom}';"
        summed_spendings = display_spendings(query)
        summed_spendings= summed_spendings[0]
        summed_spendings= summed_spendings[0]
    return render_template('monthlysummary.html', summed_spendings=summed_spendings, category=category, for_whom=for_whom)



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

def update_record(query):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()












