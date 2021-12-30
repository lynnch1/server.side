from flask import Flask, Blueprint, render_template, session
from interact_with_DB import interact_db

app = Flask(__name__)
app.secret_key = "123"

assignment10 = Blueprint('assignment10', __name__, static_folder='static', template_folder='templates')


@assignment10.route('/assignment10')
def assignment10_func():
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=users)

