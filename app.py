from flask import Flask, render_template, request
from helpers import todo

app: Flask = Flask(__name__)
todo_list: list[todo] = []
todo_count: int = 0

@app.route("/")
def index():
    return render_template('home.html')

@app.route('/post-request', methods=["GET", "POST"])
def create_todo():
    # if request.method == "POST":
    #     global todo_list
    #     global todo_count

    #     title: str = request.form['title']
    #     description: str = request.form['description']

    #     if title == '':
    #         return render_template("create-todo.html")

    #     new_todo: todo = todo(todo_count, title, description)
    #     todo_list.append(new_todo)

    #     todo_count += 1

    #     return render_template("success.html", title=title, description=description)
    return render_template("post-request.html")


@app.route('/view-todo-list')
def view_todo_list():
    return render_template('view-list.html', todo_list=todo_list)

if __name__ == '__main__':
    app.run(debug=True)

