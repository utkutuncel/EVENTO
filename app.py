from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/events')
def events_page():
    items = [
        {'no': 1, 'name': 'Techno Event 1', 'barcode': '893212299897', 'date': 'dd/mm/yy'},
        {'no': 2, 'name': 'Techno Event 2', 'barcode': '123985473165', 'date': 'dd/mm/yy'},
        {'no': 3, 'name': 'Techno Event 3', 'barcode': '231985128446', 'date': 'dd/mm/yy'}
    ]
    return render_template('/events.html', items=items)