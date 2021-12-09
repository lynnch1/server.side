from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def main_func():
    return 'Hello, This is the main page!'


@app.route('/about')
def about_func():
    return 'My name is Lynn, I am a fourth year Industrial Engineering student'


@app.route('/me')
def info_func():
    return redirect('/about')


@app.route('/help')
def not_found():
    return redirect(url_for('main_func'))


if __name__ == '__main__':
    app.run(debug=True)
