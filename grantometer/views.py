from grantometer import app
from flask import render_template, jsonify, request
from grantometer import models
from grantometer import controllers
from grantometer import db
import datetime


@app.route('/setup')
def setup():
    return "S'all good man"


@app.route('/')
def main_gauge(name=None):
    return render_template('main.html', name=name)


@app.route('/grumpy/api/v1_0', methods=['GET', 'POST'])
def manage_grumpiness():
    timestamp = datetime.datetime.now()
    gc = db.session.query(models.Grumpiness).order_by(
                       models.Grumpiness.id.desc()).first()
    grumpiness  = controllers.cool_down_grumpiness(gc.grumpiness,
                        timestamp,
                        gc.timestamp)
    if request.method == 'POST':
        data = request.get_json(force=True)
        try:
            action = data['action']
            if action == 'decrease':
                print("decrease: %s" % gc.grumpiness)
                grumpiness = controllers.decrease_grumpiness(grumpiness)
                print("to: %s" % grumpiness)
            elif action == 'increase':
                print("increase from: %s" % gc.grumpiness)
                grumpiness = controllers.increase_grumpiness(grumpiness)
                print("to: %s" % grumpiness)
        except KeyError:
            return jsonify(error="Action ist missing in" +
                                  " your request")
        except:
            return jsonify(error="Whooopsie Daysie")
        new_entry = models.Grumpiness(grumpiness, timestamp)
        db.session.add(new_entry)
        db.session.commit()
        print(new_entry)
    elif request.method == 'GET':
        print("GET")
        print('Get request: %s at %s - %s' % (grumpiness, gc.timestamp, timestamp) )
    return jsonify(grumpiness=grumpiness)

