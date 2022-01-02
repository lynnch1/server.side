from flask import Flask, Blueprint, render_template, request, redirect, session
from interact_with_DB import interact_db

app = Flask(__name__)
app.secret_key = "123"

assignment10 = Blueprint('assignment10', __name__, static_folder='static', template_folder='templates')


@assignment10.route('/assignment10')
def assignment10_func():
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=users)


@assignment10.route('/insert_user', methods=['POST'])
def insert_user_func():
    #get the data
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    #insert to db
    query = "INSERT INTO users (name, email, password) VALUES ('%s','%s','%s')" % (name, email, password)
    interact_db(query=query, query_type='commit')

    #come back to users
    return redirect('/assignment10')


@assignment10.route('/update_user', methods=['POST'])
def update_user_func():
    #get the data
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    # update db
    query = "UPDATE users SET name='%s', password='%s' WHERE email='%s';" % (name, password, email)
    interact_db(query=query, query_type='commit')

    #come back to users
    return redirect('/assignment10')


@assignment10.route('/delete_user', methods=['POST'])
def delete_user_func():
    user_id = request.form['id']
    query = "DELETE FROM users WHERE id='%s';" % user_id
    interact_db(query=query, query_type='commit')

    return redirect('/assignment10')
