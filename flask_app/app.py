from flask import Flask, render_template

app=Flask(__name__)

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
