from flask import Blueprint, render_template

import requests
import os

lemmy = Blueprint('lemmy', __name__)

employees = [
    { 'name': 'KunhaiG', 'title': 'Python Amateur', 'image': 'lemmy-kunhaig.png', 'quote': 'Team?', },
    { 'name': 'LuckyLachy', 'title': 'Executive Memeographer', 'image': 'lemmy-luckylachy.png', 'quote': 'You know that saying that there are no bad questions? Well, there are, and this is one of them.', },
    { 'name': 'Chesty', 'title': 'Memeographer', 'image': 'lemmy-chesty.png', 'quote': '[Crackling]', },
    { 'name': 'Dragons_Ire', 'title': 'Executive Contractor', 'image': 'lemmy-dragonsire.png', 'quote': 'I have trouble following basic instructions.', },
    { 'name': 'UncleLawyer', 'title': 'Legal Counsel', 'image': 'lemmy-unclelawyer.png', 'quote_class': 'small', 'quote': 'Qualified to provide legal advice, but only with supervision and through a law firm. This does not constitute legal advice with respect to the legality of providing legal advice. If you have any legal questions, you should consult a legal practicioner.', },
    { 'name': 'RikerZZZ', 'title': 'Assistant Creative Advisor', 'image': 'lemmy-rikerzzz.png', 'quote': 'What\'s the circumstances?', },
    { 'name': 'HotBotGG', 'title': 'Assistant Lemmy', 'image': 'lemmy-hotbotgg.png', 'quote': 'Mafia is love. Mafia is life.', },
    { 'name': 'Your Name Here', 'title': 'Excited New Recruit', 'image': 'lemmy-scott.png', 'quote': 'We\'re Hiring!', },
]

@lemmy.route('/lemmy/')
def index():

    # get list of emotes and stickers from Github
    emotes = requests.get(
        'https://api.github.com/repos/halbrd/Lemmy/contents/static/Emoters/emote',
        headers={'Authorization': 'token ' + os.environ['LYNQME_GITHUB_TOKEN']}
    ).json()
    emotes = sorted(emotes, key=lambda emote: emote['name'].lower())

    stickers = requests.get(
        'https://api.github.com/repos/halbrd/Lemmy/contents/static/Emoters/sticker',
        headers={'Authorization': 'token ' + os.environ['LYNQME_GITHUB_TOKEN']}
    ).json()
    stickers = sorted(stickers, key=lambda sticker: sticker['name'].lower())

    def emoter_filename_to_chunks(emoter_filename):
        ''' Example: 'FreeFormJazz.png' -> ['Free', 'Form', 'Jazz'] '''
        # strip extension, or use whole filename if it has no extension
        emoter_name = ''.join(emoter_filename.split('.')[:-1]) or emoter_filename

        # add a space before each capital letter
        with_spaces = [ (' ' + char) if char.isupper() else char for char in emoter_name ]

        # convert to list of chunks
        emoter_chunks = ''.join(with_spaces).strip().split()

        return emoter_chunks

    def expand_emoter(emoter):
        return {
            'name': emoter_filename_to_chunks(emoter['name']),
            # TODO: resize these images and cache them, to save bandwidth
            'url': f'https://raw.githubusercontent.com/halbrd/Lemmy/master/' + emoter['path'],
        }

    # expand filenames to display name and url
    emotes = list(map(expand_emoter, emotes))
    stickers = list(map(expand_emoter, stickers))

    # sort stickers
    stickers_normal = []
    stickers_lolfb = []
    stickers_teams = []

    for sticker in stickers:
        if sticker['name'][0] == 'Fb':
            stickers_lolfb.append(sticker)
        elif sticker['name'][0] == 'Team':
            stickers_teams.append(sticker)
        else:
            stickers_normal.append(sticker)


    return render_template('lemmy/index.html',
        emotes=emotes,
        stickers_normal=stickers_normal,
        stickers_lolfb=stickers_lolfb,
        stickers_teams=stickers_teams,
        employees=employees,
    )
