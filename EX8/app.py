from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run()
