from flask import Blueprint, render_template

bts = Blueprint('bts', __name__)

@bts.route('/bts/')
def index():
    return render_template('bts/index.html')
