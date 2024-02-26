from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    # Example list of servants
    servantinfo = [
        {'name': 'Altria Pendragon', 'level': 90, 'grailed': 'Yes', 'skill_levels': '10/10/10', 'rarity': '5*'},
        {'name': 'Gilgamesh', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '5*'},
        # Add more servants as needed
    ]
    return render_template('home.html', servantinfo=servantinfo)


if __name__ == '__main__':
    app.run(debug=True)
