from flask import Flask, jsonify, redirect
from json import JSONEncoder

app = Flask(__name__)


class Numbers:
    def __init__(self, total):
        self.total = total

#We use the JSONEncoder to serialize the class.
class NumberEncoder(JSONEncoder):
    def default(self, o):
         return o.__dict__

@app.route("/")
def redirect():
    return redirect('/total')

# Just added the default param to be able to create the test of the method
@app.route('/total',defaults={'data': None}, methods=['GET'])
def get_sum(data):
    numbers_to_add = list(range(10000001))
    x = 0
    #Just added the if to test the method
    if data is None:
        for num in numbers_to_add:
            x += num
            res = Numbers(x)
        return jsonify(NumberEncoder().encode(res))
    else:
        for num in data:
            x += num
        return x

if __name__ == '__main__':
    app.run(debug=True)
