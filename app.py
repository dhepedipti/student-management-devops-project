from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
students = []
next_id = 1

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Management Portal</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f2f5f9; margin: 40px; }
        .container { max-width: 850px; margin: auto; background: white; padding: 25px; border-radius: 10px; }
        h1 { color: #17365d; }
        input, button { padding: 10px; margin: 5px; }
        button { background: #17365d; color: white; border: none; cursor: pointer; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 10px; text-align: left; }
        th { background: #17365d; color: white; }
        .delete { background: #c62828; }
    </style>
</head>
<body>
<div class="container">
    <h1>Student Management Portal</h1>
    <p>Manage student records using this web application.</p>
    <h3>Add Student</h3>
    <form action="/add" method="POST">
        <input type="text" name="name" placeholder="Student Name" required>
        <input type="email" name="email" placeholder="Email Address" required>
        <input type="text" name="course" placeholder="Course" required>
        <button type="submit">Add Student</button>
    </form>
    <h3>Student Records</h3>
    <table>
        <tr><th>ID</th><th>Name</th><th>Email</th><th>Course</th><th>Action</th></tr>
        {% for student in students %}
        <tr>
            <td>{{ student.id }}</td>
            <td>{{ student.name }}</td>
            <td>{{ student.email }}</td>
            <td>{{ student.course }}</td>
            <td>
                <form action="/delete/{{ student.id }}" method="POST">
                    <button class="delete" type="submit">Delete</button>
                </form>
            </td>
        </tr>
        {% endfor %}
    </table>
</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, students=students)

@app.route("/add", methods=["POST"])
def add_student():
    global next_id
    student = {
        "id": next_id,
        "name": request.form["name"],
        "email": request.form["email"],
        "course": request.form["course"]
    }
    students.append(student)
    next_id += 1
    return redirect("/")

@app.route("/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    global students
    students = [s for s in students if s["id"] != student_id]
    return redirect("/")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
