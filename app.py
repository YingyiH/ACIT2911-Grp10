from flask import Flask, render_template, request, redirect, url_for, flash
import os
import json

app = Flask(__name__)
app.secret_key = "sdfsanfdjksdbafkjsah"


@app.route('/')
def homepage():
    return render_template('/home.html')


@app.route('/products')
def products():
    return render_template('/products.html')


@app.route('/admin')
def admin():
    return render_template('admin-login.html')


@app.route('/about')
def about():
    return redirect


@app.route('/admin/dashboard', methods=['POST'])
def dashboard():
    if request.method == 'POST':
        email, password = request.form['email'], request.form['password']
        with open('creds.json', 'r') as creds:
            admin_list = json.loads(creds.read())
            for admin in admin_list:
                if email == admin['email'] and password == admin['password']:
                    return render_template('admin_dashboard.html', user=admin['name'])
                else:
                    flash("Incorrect email or password. Try Again..")
                    return redirect('/admin')


if __name__ == "__main__":
    app.run(debug=True)
