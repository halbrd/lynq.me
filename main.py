from flask import Flask, render_template

from views.lemmy import lemmy
from views.skyrim import skyrim
from views.bts import bts

app = Flask(__name__)

app.register_blueprint(lemmy)
app.register_blueprint(skyrim)
app.register_blueprint(bts)

@app.route('/')
def index():
    pages = [
        { 'title': 'lemmy',             'location': '/lemmy' },
        { 'title': 'discord server',    'location': '/bts' },
        { 'title': 'personal site',     'location': 'https://halbrd.com' },
        { 'title': 'professional site', 'location': 'https://will.sx' },
    ]
    return render_template('index.html', pages=pages)

if __name__ == '__main__':
    # debug mode - not for production
    app.run(host='0.0.0.0', debug=True, port=5000)
