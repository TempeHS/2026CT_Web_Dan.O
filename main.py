from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
    card_data = (
        ("Saxophone", "saxophones", "come for saxophones", "static/images/Card_1.png"),
        ("Learn Saxophone", "Want to learn how to play saxophone", "Click for skills", "static/images/Card_2.png"),
        ("Basic skills", "Why a saxophone will fix your life", "I'll help you", "static/images/Card_6.png"),
        ("Music Theory", "Want to basic music knowledge", "come for saxophones", "static/images/Card_3.png"),
        ("Bands", "How saxophones shaped jazz bands", "come for saxophones", "static/images/Card_5.png"),
        ("Jazz", "Jazz Saxophones", "You like jazz", "static/images/Card_4.png"),
    )
    return render_template("index.html", cards=card_data), 200


@app.route('/contact.html')
def contact():
    return render_template('contact.html'), 200


@app.route('/questions.html')
def questions():
    return render_template('questions.html'), 200


@app.route('/tutoring.html')
def tutoring():
    return render_template('tutoring.html'), 200


@app.route('/BS.html')
def BS():
    return render_template('BS.html'), 200



if __name__ == '__main__':
    app.run(debug=True)