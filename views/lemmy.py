from flask import Blueprint, render_template

import requests

lemmy = Blueprint('lemmy', __name__)

@lemmy.route('/lemmy/')
def index():

    # get list of emotes and stickers from Github
    emotes = requests.get('https://api.github.com/repos/halbrd/Lemmy/contents/lemmy-2/static/Emoters/emote').json()

    def emote_filename_to_chunks(emote_filename):
        # strip extension, or use whole filename if it has no extension
        emote_name = ''.join(emote_filename.split('.')[:-1]) or emote_filename

        # add a space before each capital letter
        with_spaces = [ (' ' + char) if char.isupper() else char for char in emote_name ]

        # convert to list of chunks
        emote_chunks = ''.join(with_spaces).strip().split()

        return emote_chunks

    # expand filenames to display name and url
    emotes = [ {
        'name': emote_filename_to_chunks(emote['name']),
        'url': 'https://raw.githubusercontent.com/halbrd/Lemmy/master/lemmy-2/static/Emoters/emote/' + emote['name'],
    } for emote in emotes ]

    return render_template('lemmy/index.html',
        emotes=emotes,
        stickers=stickers,
    )
