from grantometer import app
from flask import render_template, jsonify, request, json


@app.route('/')
def main_gauge(name=None):
    return render_template('main.html', name=name)


@app.route('/grumpy_api/v1.0', methods=['GET', 'POST'])
def manage_grumpyness():
    if request.method == 'POST':
        data = request.get_json(force=True)
        with open('count.txt', 'w+') as f:
            f.write(str(data['grantigkeit']))
        return json.dumps(data)
    else:
        with open('count.txt', 'r') as f:
            grant = None
            for line in f:
                grant = line
        return jsonify(grantigkeit=grant)
