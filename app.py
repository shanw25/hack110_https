from random import randint
from flask import Flask, render_template, request, redirect
from utility.helpers import todo, User


app: Flask = Flask(__name__)
todo_list: list[todo] = []
todo_count: int = 0
user_count: int = 0
current_user: User = None
users: list[User] = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        global current_user
        global user

        id: int = user_count
        name: str = request.form['name']
        if name == "":
            return render_template('login.html')

        current_user = User(id, name)
        users.append(current_user)
    if current_user == None:
        return render_template('login.html')
    return render_template('index.html', todo_list=todo_list)

@app.route('/post-request', methods=["GET", "POST"])
def create_todo():
    if request.method == "POST":
        global todo_list
        global todo_count

        id: int = todo_count
        title: str = request.form['title']
        description: str = request.form['description']
        time: str = request.form['time']
        location: str = request.form['location']
        number: int = request.form['number']
        tag: str = request.form['tag']
        tag  = "#" + tag
        host = current_user
        participants: list[User] = [] # a list of User()


        if title == '':
            return render_template("create-todo.html")

        new_event: todo = todo(id, title, description, time, location, number, tag, host, participants)
        todo_list.append(new_event)

        todo_count += 1
        # print(len(todo_list))
        return redirect('/')
    return render_template("post-request.html")


@app.route('/view-todo-list')
def view_todo_list():
    return render_template('view-list.html', todo_list=todo_list)


@app.route("/log-out", methods=["GET"])
def log_out():
    global current_user

    current_user = None
    return redirect('/')


@app.route("/join", methods=["POST"])
def join():
    global current_user
    current_id = request.form('id')
    if (current_user.name == todo_list[current_id].host) or (current_user in todo_list[current_id].participants):
        return render_template("join-fail.html")
    todo_list[current_id].participants.append(current_user)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

