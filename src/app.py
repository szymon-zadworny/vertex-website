from asgiref.wsgi import WsgiToAsgi
from flask import Flask, render_template, url_for, send_from_directory
from converter import get_articles

app = Flask(__name__)
asgi_app = WsgiToAsgi(app)

blog = get_articles("content/blog")

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/council')
def council():
    return render_template('council.html')
