from grantometer import app
from flask import render_template, jsonify, request
from grantometer import models
from grantometer import controllers
from grantometer import db
import datetime
import uuid


@app.route('/setup')
def setup():
    with app.app_context():
        db.create_all()
    new_entry = models.Grumpiness(0, datetime.datetime.now())
    db.session.add(new_entry)
    db.session.commit()
    return "S'all good man"


@app.route('/')
def main_gauge(name=None):
    return render_template('main.html', name=name)


@app.route('/api/v1_1/grumpy/', methods=['GET', 'POST'])
def manage_grumpiness():
    timestamp = datetime.datetime.now()
    gc = db.session.query(models.Grumpiness).order_by(
         models.Grumpiness.id.desc()).first()
    grumpiness = controllers.cool_down_grumpiness(gc.grumpiness,
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
        try:
            guid = data['guid']
        except KeyError:
            return jsonify(error="Guid missing")
        except:
            return jsonify(error="Whooooopsie Daysie! Wrong hole!")
        try:
            models.save_new_grumpiness(grumpiness, guid, timestamp)
            print("Guid %s" % guid)
        except:
            return jsonify("DB writign failed")
    elif request.method == 'GET':
        print("GET")
        print('Get request: %s at %s - %s' % (grumpiness, gc.timestamp,
                                              timestamp))
    return jsonify(grumpiness=grumpiness)


@app.route('/api/v1_1/grumpyID/', methods=['GET'])
def send_uuid():
    return jsonify(guid=uuid.uuid4())
