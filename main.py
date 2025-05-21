from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
    card_data = (
        ("Saxophone", "saxophones", "come for saxophones", "static/images/logo.png"),
        ("Learn Saxophone", "Want to learn how to play saxophone", "Click for topic", "static/images/logo.png"),
        ("Saxophone", "Why a saxophone will fix your life", "I'll help you", "static/images/logo.png"),
        ("Saxophone", "Want to basic music knowledge", "come for saxophones", "static/images/logo.png"),
    )
    return render_template("index.html", cards=card_data), 200


if __name__ == '__main__':
    app.run(debug=True)