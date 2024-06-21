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
        "url": os.getenv("URL"),
        "work_experience_1": "Undergraduate Researcher at Communications @ UCSB (2023-2024)",
        "work_experience_2": "Full Stack Development Intern at MOVE Lab @ UCSB (2023)",
        "work_experience_3": "Software Engineer Intern at Motivo (2022)",
        "education_1": "B.S. in Statistics and Data Science, UCSB (Expected 2027)",
        "education_2": "High School Diploma, Oak Ridge High School (2019-2023)"
    }

    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run(debug=True)