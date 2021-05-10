import json
import base64
from flask import Flask, request, jsonify
from io import BytesIO

from gui import GalaxyPlot

app = Flask(__name__)


@app.route('/clima')
def clima():
    with open('data.json') as f:
        data = json.load(f)
    dia = request.args.get('dia') or '1'
    return jsonify(data[dia])


@app.route('/')
def index():
    return '''It works! <br/><br/>
        GET clima: <a href='{url}clima?dia=1'>{url}clima?dia=1</a> <br/>
        GET imagen: <a href='{url}imagen?dia=79'>{url}imagen?dia=79</a>
    '''.format(url=request.url_root)


@app.route('/imagen')
def image():
    dia = int(request.args.get('dia')) or 1
    plot = GalaxyPlot(day=dia)
    plot.set_title('Meli galaxy')

    buf = BytesIO()
    plot.fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
