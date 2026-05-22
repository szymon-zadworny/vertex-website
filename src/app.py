from asgiref.wsgi import WsgiToAsgi
from flask import Flask, render_template, url_for, send_from_directory

app = Flask(__name__)
asgi_app = WsgiToAsgi(app)

@app.route("/")
def display_player():
    return render_template('player.html', src=url_for('static', filename='video/video.mpd'))

@app.route('/video/<path:path>')
def get_static(path):
    return send_from_directory('static/video', path)
