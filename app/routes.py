from flask import (
    Flask,
    render_template,
    request
)

import requests

BACKEND_URL = "http://127.0.0.1:5000/tasks"
app = Flask(__name__)

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/about")
def about_me():
    me = {                              #dictionary
        "first_name": "Samantha",       #Key value paries
        "last_name": "Roman",
        "hobbies": "Shopping"
    }
    return render_template("about.html", user=me)

@app.get("/tasks")
def display_task_list():
    response = requests.get(BACKEND_URL)
    if response.status_code == 200:
        task_list = response.json().get("tasks")
        return render_template("list.html", tasks=task_list)
    return (
        render_template("error.html", err=response.status_code),
        response.statuse_code
    )

@app.get("/tasks/<int:pk>/edit")
def render_edit_form(pk):
    url = "%s/%s" % (BACKEND_URL, pk)
    response = requests.get(url)
    if response.status_code == 200:
        task_data = response.json().get("task")
        return render_template("edit.html", task=task_data)
    return (
        render_template("error.html", err=response.status_code),
        response.status_code
    )

@app.post("/tasks/<int:pk>/edit")
def edit_task(pk):
    url = "%s/%s" % (BACKEND_URL, pk)
    task_data = request.form
    response = requests.put(url, json=task_data)
    if response.status_code == 204:
        return render_template("success.html")
    return (
        render_template("error.html", err=response.status_code),
        response.status_code
    )

@app.get("/tasks/<int:pk>/create")
def render_new_task(pk):
    url = "%s/%s" % (BACKEND_URL, pk)
    response = requests.get(url)
    if response.status_code == 200:
        task_data = response.json().get("task")
        return render_template("create.html", task=task_data)
    return (
        render_template("error.html", err=response.status_code),
        response.status_code
    )

@app.post("/tasks/<int:pk>/create")
def create_task(pk):
    url = "%s/%s" % (BACKEND_URL, pk)
    task_data = request.form
    response = requests.put(url, json=task_data)
    if response.status_code == 204:
        return render_template("success.html")
    return (
        render_template("error.html", err=response.status_code),
        response.status_code
    )



