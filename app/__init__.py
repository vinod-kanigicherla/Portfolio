import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    context = {
        "title": "Vinod Kanigicherla",
        "about_me": "Hi! I'm Vinod, a student at UCSB majoring in Statistics and Data Science. I am deeply interested in the intersection of data science, computer science, and software engineering, with a particular focus on machine learning and its practical applications for solving real-world challenges.",
        "url": os.getenv("URL")
    }

    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run(debug=True)