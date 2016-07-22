from grantometer import app
from flask import render_template, jsonify, request
from grantometer import models
from grantometer import controllers
from grantometer import db
import datetime


@app.route('/setup')
def setup():
    db.create_all()
    db.session.add(models.Grumpiness(1))
    db.session.commit()
    return "S'all good man"


@app.route('/')
def main_gauge(name=None):
    return render_template('main.html', name=name)


@app.route('/grumpy/api/v1_0', methods=['GET', 'POST'])
def manage_grumpiness():
    gc = db.session.query(models.Grumpiness).order_by(
                       models.Grumpiness.id.desc()).first()
    timestamp = datetime.datetime.now()
    grumpiness  = controllers.cool_down_grumpiness(gc.grumpiness,
                        timestamp,
                        gc.timestamp)
    if request.method == 'POST':
        data = request.get_json(force=True)
        try:
            action = data['action']
            if action == 'decrease':
                grumpiness = controllers.decrease_grumpiness(grumpiness)
            elif action == 'increase':

                grumpiness = controllers.increase_grumpiness(grumpiness)
                print(grumpiness)
        except KeyError:
            return jsonify(error="Action ist missing in" +
                                  " your request")
        except:
            return jsonify(error="Whooopsie Daysie")
        db.session.add(models.Grumpiness(grumpiness))
        db.session.commit()
    elif request.method == 'GET':
        db.session.add(models.Grumpiness(grumpiness))
        db.session.commit()
    return jsonify(grumpiness=grumpiness)
