from flask import Flask

app = Flask(__name__)

employees = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Ravi"},
    {"id": 3, "name": "Priya"}
]

@app.route("/")
def home():
    return """
    <h1>Employee Management Portal</h1>
    <h2>Employee List</h2>
    <ul>
        <li>John</li>
        <li>Ravi</li>
        <li>Priya</li>
    </ul>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)