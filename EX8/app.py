from flask import Flask, render_template
from flask import request
from flask import session

app = Flask(__name__)
app.secret_key = '123'


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

            findUser=''
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


if __name__ == '__main__':
    app.run()
