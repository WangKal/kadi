from flask import Blueprint, render_template, request, session

web_bp = Blueprint('web_bp', __name__)

@web_bp.route('/')
def home():
    return render_template('index.html')

@web_bp.route('/register', methods=['GET', 'POST'])
def register():
    # Handle registration logic here
    return render_template('register.html')

@web_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Handle login logic here
    return render_template('login.html')

@web_bp.route('/waiting_bay')
def waiting_bay():
    # Handle waiting bay logic here
    challenge_link = session['sharing_url']
    challenge = session['challenge']
    challengeID = session['challengeID']
    return render_template('waiting_bay.html', challenge_link=challenge_link, challenge=challenge, challengeID=challengeID)

@web_bp.route('/kadi_invite/<link>', methods=['GET'])
def kadi_invite(link):
    # Handle waiting bay logic here
    challenge_link = link
    return render_template('kadi_accept_invite.html', challenge_link=challenge_link)


@web_bp.route('/play')
def play():
    # Handle play logic here
    play_status = request.args.get('play_status')
    plays = request.args.getlist('plays')
    my_cards = request.args.getlist('my_cards')

    if play_status == 'playing':
        to_start = plays[-1] if isinstance(plays, list) else plays
    else:
        to_start = None

    return render_template('play.html', play_status=play_status, to_start=to_start, my_cards=my_cards)
