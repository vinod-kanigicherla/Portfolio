import datetime
import os

from dotenv import load_dotenv
from flask import Flask, render_template, request
from peewee import *
from playhouse.shortcuts import model_to_dict

load_dotenv()

app = Flask(__name__)

mydb = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306,
)
print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

@app.route("/")
def home():
    context = {"title": "Vinod Kanigicherla", "url": os.getenv("URL")}
    return render_template("home.html", **context)

@app.route("/about")
def about():
    context = {
        "title": "Vinod Kanigicherla",
        "about_me": "Hi! I'm Vinod, a student at UCSB majoring in Computer Science. I am deeply interested in the intersection of data science, computer science, and software engineering, with a particular focus on machine learning and its practical applications for solving real-world challenges.",
        "work_experiences": [
            {"role": "Undergraduate Researcher at Communications @ UCSB", "duration": "2023-2024"},
            {"role": "Full Stack Development Intern at MOVE Lab @ UCSB", "duration": "2023"},
            {"role": "Software Engineer Intern at Motivo", "duration": "2022"},
        ],
        "education": [
            {"degree": "B.S. in Statistics and Data Science, UCSB", "duration": "Expected 2027"},
            {"degree": "High School Diploma, Oak Ridge High School", "duration": "2019-2023"},
        ],
    }
    return render_template("about.html", **context)

@app.route("/hobbies")
def hobbies():
    context = {
        "title": "Vinod Kanigicherla",
        "hobbies": [
            {"name": "Drumming", "image": "drums.jpg"},
            {"name": "Hiking", "image": "hiking.jpg"},
        ],
    }
    return render_template("hobbies.html", **context)

@app.route("/places")
def places():
    context = {"title": "Vinod Kanigicherla"}
    return render_template("places.html", **context)

@app.route("/api/timeline_post", methods=["POST"])
def post_time_line_post():
    name = request.form["name"]
    email = request.form["email"]
    content = request.form["content"]
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

@app.route("/api/timeline_post", methods=["GET"])
def get_time_line_post():
    return {
        "timeline_posts": [
            model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route("/api/timeline_post/<int:post_id>", methods=["DELETE"])
def delete_time_line_post(post_id):
    timeline_post = TimelinePost.get_by_id(post_id)
    timeline_post.delete_instance()
    return model_to_dict(timeline_post)


# Run the application
if __name__ == "__main__":
    app.run(debug=True)
    