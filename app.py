from flask import Flask, render_template, jsonify

app = Flask(__name__)

servants = [
    {'name': 'Altria Pendragon', 'level': 100, 'grailed': 'Yes', 'skill_levels': '10/10/10', 'rarity': '5*'},
    {'name': 'Hassan i Sabbah', 'level': 100, 'grailed': 'Yes', 'skill_levels': '9/9/6', 'rarity': '5*'},
    {'name': 'Enkidu', 'level': 98, 'grailed': 'Yes', 'skill_levels': '9/6/6', 'rarity': '5*'},
    {'name': 'Dioscuri', 'level': 90, 'grailed': 'No', 'skill_levels': '6/6/6', 'rarity': '5*'},
    {'name': 'Zhuge Liang', 'level': 90, 'grailed': 'No', 'skill_levels': '6/3/10', 'rarity': '5*'},
    {'name': 'Morgan', 'level': 100, 'grailed': 'Yes', 'skill_levels': '10/10/10', 'rarity': '5*'},
    {'name': 'Ashiya Douman', 'level': 100, 'grailed': 'Yes', 'skill_levels': '10/10/10', 'rarity': '5*'},
    {'name': 'Napoleon', 'level': 90, 'grailed': 'No', 'skill_levels': '7/7/7', 'rarity': '5*'},
    {'name': 'Nightingale (Archer)', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Nightingale (Berserker)', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '5*'},
    {'name': 'Odysseus', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '5*'},
    {'name': 'BB', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Koyanskaya', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '5*'},
    {'name': 'Yang Guifei', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '5*'},
    {'name': 'Karna (Santa)', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Artoria Alter', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Tam Lin Tristan', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Yu Mei-ren', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Elisabeth Bathory', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Caster Gilgamesh', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Kiichi Hogen', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Heracles', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Astraea', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Hessian Lobo', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Mysterious Idol X (Alter)', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Mash', 'level': 80, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '3*'},
    {'name': 'Calamity Jane', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Yagyu Tajima no Kami Munenori', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Altria Lily', 'level': 80, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Siegfried', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Percival', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': "Jeanne d'Arc", 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '5*'},
    {'name': 'Medusa (Lancer)', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Carmilla', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Martha', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Atlante (Alter)', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Suzuka Gozen', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Stheno', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Barghest', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Saito Hajime', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Lan Ling', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Diarmuid Ua Duibhne', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Frankenstein (Saber)', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Chiron', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Caenis', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '5*'},
    {'name': 'Vlad III', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '5*'},
    {'name': 'Osakabehime', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Penthesilea', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Ibaraki Douji', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '4*'},
    {'name': 'Ganesha', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '5*'},
    {'name': 'Angra Mainyu', 'level': 90, 'grailed': 'No', 'skill_levels': '10/10/10', 'rarity': '0*'},
]


@app.route('/')
def home():
    return render_template('home.html', servantinfo=servants)


@app.route('/servantsinfo')
def about():
    return render_template('servantsinfo.html', servantinfo=servants)


@app.route('/api/servants')
def servantapi():
    return jsonify(servants)


@app.route('/abouts')
def abouts():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
