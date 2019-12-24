from flask import Blueprint, render_template

lemmy = Blueprint('lemmy', __name__)

@lemmy.route('/lemmy/')
def index():
    return render_template('lemmy/index.html')
