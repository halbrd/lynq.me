from flask import Flask, render_template

from views.lemmy import lemmy
from views.skyrim import skyrim

app = Flask(__name__)

app.register_blueprint(lemmy)
app.register_blueprint(skyrim)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # debug mode - not for production
    app.run(host='0.0.0.0', debug=True, port=5000)
