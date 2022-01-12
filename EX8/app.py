from flask import Flask, render_template, request, session
from flask import jsonify
import mysql, mysql.connector
import requests
from interact_with_DB import interact_db

app = Flask(__name__)
app.secret_key = '123'

# assignment10
from assignment10.assignment10 import assignment10

app.register_blueprint(assignment10)


@app.route('/')
@app.route('/home')
def main_func():
    return render_template('CVgrid.html')


@app.route('/Exercise2')
def about1():
    return render_template('exercise2.html')


@app.route('/Form')
def info():
    return render_template('forms.html')


@app.route('/Assignment8')
def assignment8():
    hobbies = ['eating', 'sleeping', 'netflix', 'friends']
    hobby = 'sleeping'
    return render_template('assignment8.html', hobbies=hobbies, hobby=hobby)


@app.route('/Assignment9', methods=['GET', 'POST'])
def assignment9():
    users = {'user1': {'name': 'Yossi', 'email': 'yo@gmail.com'},
             'user2': {'name': 'Lynn', 'email': 'lynn@gmail.com'},
             'user3': {'name': 'Yarin', 'email': 'yarin@gmail.com'},
             'user4': {'name': 'Rahav', 'email': 'Rahav@gmail.com'},
             'user5': {'name': 'Doron', 'email': 'doron@gmail.com'},
             'user6': {'name': 'Carmit', 'email': 'carmit@gmail.com'}}

    if request.method == 'GET':
        if 'Search' in request.args:
            search = request.args['Search']
            if search == '':
                return render_template('assignment9.html', users=users)

            findUser = ''
            i = 1
            for user in users.values():
                if user['email'] == search or user['name'] == search:
                    findUser = user
                i += 1
            if len(findUser) != 0:
                return render_template('assignment9.html', userFound=findUser)
            else:
                return render_template('assignment9.html', NotFound='sorry, user not found')
        else:
            return render_template('assignment9.html')

    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['username'] = username
        return render_template('assignment9.html', username=username)


@app.route('/logout')
def logout_func():
    session['username'] = ''
    return render_template('assignment9.html')


# assignment 11
@app.route('/assignment11/users', methods=['GET'])
def get_users_func():
    query = "select * from users"
    users = interact_db(query=query, query_type='fetch')
    users_dict = {}
    for user in users:
        users_dict[f'user id: {user.id}'] = {
            'name': user.name,
            'email': user.email
        }
    return jsonify(users_dict)


def extract_user(num):
    res = requests.get(f'https://reqres.in/api/users/{num}')
    res = res.json()
    return res


@app.route('/assignment11/outer_source', methods=['GET', 'POST'])
def outer_source_backend_func():
    if "number" in request.args:
        num = int(request.args['number'])
        user = extract_user(num)
        return render_template('assignment11-outer_source.html', user=user)
    else:
        return render_template('assignment11-outer_source.html')


@app.route('/assignment12/restapi_users', defaults={'user_id': -1})
@app.route('/assignment12/restapi_users/<int:user_id>')
def get_users(user_id):
    if user_id == -1:
        return_dict = {}
        query = 'select * from users;'
        users = interact_db(query=query, query_type='fetch')
        for user in users:
            return_dict[f'user_{user.id}'] = {
                'status': 'success',
                'name': user.name,
                'email': user.email,
            }
    else:
        query = 'select * from users where id=%s;' % user_id
        users = interact_db(query=query, query_type='fetch')
        if len(users) == 0:
            return_dict = {
                'status': 'failed',
                'message': 'user not found'
            }
        else:
            return_dict = {
                'status': 'success',
                'id': users[0].id,
                'name': users[0].name,
                'email': users[0].email,
            }
    return jsonify(return_dict)


if __name__ == '__main__':
    app.run()
