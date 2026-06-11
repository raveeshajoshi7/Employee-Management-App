from flask import Flask

app = Flask(__name__)

employees = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Ravi"},
    {"id": 3, "name": "Priya"}
]

@app.route("/")
def home():
    employee_html = ""

    for emp in employees:
        employee_html += f"<li>{emp['id']} - {emp['name']}</li>"

    return f"""
    <h1>Employee Management Portal - Version 2</h1>
    <h2>Employee List</h2>
    <ul>
        {employee_html}
    </ul>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)