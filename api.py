import json
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/clima')
def clima():
    with open('data.json') as f:
        data = json.load(f)
    dia = request.args.get('dia') or '1'
    return jsonify(data[dia])


@app.route('/')
def index():
    return 'It works! %sclima?dia=1' % request.url_root


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
