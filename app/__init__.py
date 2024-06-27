import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def home():
    context = {
        "title": "Vinod Kanigicherla",
        "url": os.getenv("URL")
    }
    return render_template('home.html', **context)

@app.route('/about')
def about():
    context = {
        "title": "Vinod Kanigicherla",
        "about_me": "Hi! I'm Vinod, a student at UCSB majoring in Computer Science. I am deeply interested in the intersection of data science, computer science, and software engineering, with a particular focus on machine learning and its practical applications for solving real-world challenges.",
        "work_experiences": [
            {"role": "Undergraduate Researcher at Communications @ UCSB", "duration": "2023-2024"},
            {"role": "Full Stack Development Intern at MOVE Lab @ UCSB", "duration": "2023"},
            {"role": "Software Engineer Intern at Motivo", "duration": "2022"}
        ],
        "education": [
            {"degree": "B.S. in Statistics and Data Science, UCSB", "duration": "Expected 2027"},
            {"degree": "High School Diploma, Oak Ridge High School", "duration": "2019-2023"}
        ]
    }
    return render_template('about.html', **context)

@app.route('/hobbies')
def hobbies():
    context = {
        "title": "Vinod Kanigicherla",
        "hobbies": [
            {"name": "Drumming", "image": "drums.jpg"},
            {"name": "Hiking", "image": "hiking.jpg"}
        ]
    }
    return render_template('hobbies.html', **context)

@app.route('/places')
def places():
    context = {
        "title": "Vinod Kanigicherla"
    }
    return render_template('places.html', **context)

if __name__ == '__main__':
    app.run(debug=True)