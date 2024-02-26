from flask import Flask, render_template, jsonify

app = Flask(__name__)

servantinfo = [
    {'name': 'Altria Pendragon', 'level': 90, 'grailed': 'Yes', 'skill_levels': '10/10/10', 'rarity': '5*'},
    {'name': 'Gilgamesh', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '5*'},
    # Add more servants as needed
]


@app.route('/')
def home():
    return render_template('home.html', servantinfo=servantinfo)


@app.route('/api/servants')
def servantdata():
    return jsonify(servantinfo)


if __name__ == '__main__':
    app.run(debug=True)
