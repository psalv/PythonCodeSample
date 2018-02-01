from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return "Hi.<br><br>" \
           "This is a coding sample written for Lyft by Paul Salvatore.<br><br>" \
           "It's functionality can be tested with the following command line command:<br><br><br>" \
           "<b>curl -X POST http://pythoncodingsample.herokuapp.com/test --data '{\"x\": 4, \"y\": 2}'" \
           "-H 'Content-Type: application/json'</b>"


@app.route('/test', methods=['POST'])
def test():
    sent_data = request.get_json()
    x = sent_data['x']
    y = sent_data['y']

    if type(x) is int and type(y) is int:
        return jsonify({'sum': x + y})
    else:
        return jsonify({'Invalid parameters': 'Please enter valid integers'})


if __name__ == "__main__":
    app.run()
