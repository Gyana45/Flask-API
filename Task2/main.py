"""
Create a table
Insert
Update
Bulk insert
Delete
download

"""
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@app.route("/table_operation", methods=['POST'])
def operation():
    if request.method == "POST":
        operation = request.form['operation']
        if operation == "create":
            return render_template("/create.html")


if __name__ == '__main__':
    app.run(port=1111)
