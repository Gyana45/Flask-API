from flask import Flask, request, jsonify

app = Flask(__name__)  # create an object of Flask class
# print(app)
# print(type(app))

"""
if i am trying call wow() from somewhere else
first of all it need to reach out to this location(test.py).
so we need the address/url--so creating route.

Accessibility & security:
----------------------------
GET: sending data (public query)
POST: sending data privately(sending username,pwd to authenticate)

"""


@app.route("/gyan_first_apitest", methods=['GET', 'POST'])
def wow():
    # if its sending data by body/securely
    if request.method == 'POST':
        a = request.json['no1']
        b = request.json['no2']
        result = a + b
        return jsonify(result)  # json format


@app.route("/gyana/hi", methods=['GET', 'POST'])
def hi():
    name = request.get_data('name')

    return jsonify("Hi " + name)


if __name__ == '__main__':
    app.run() # app.run(port=1111)

"""
def wow(a, b):
    print(a + b)
    return a + b


wow(4, 5)
"""

# pip install flask---in ApiTest env
# flask --version
# flask will convert function into api
# convert wow into api using flask
# call wow function from postman
