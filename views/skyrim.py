from flask import Blueprint, render_template

skyrim = Blueprint('skyrim', __name__)

@skyrim.route('/skyrim/')
def index():
    return render_template('skyrim/index.html')
