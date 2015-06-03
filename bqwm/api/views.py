from flask import request, json

from bqwm.api import app
from bqwm.schedulers import createReservation


@app.route('/v2.0/addManager', methods=['POST'])
def api2_addManager():
    return json.dumps({})


@app.route('/v2.0/getConfigurationCost', methods=['POST'])
def api2_getConfigurationCost():
    return json.dumps({"Costs": []})


@app.route('/v2.0/createReservation', methods=['POST'])
def api2_createReservation():

    jobdesc = {}

    if request.headers['Content-Type'] == 'application/json':
        if isinstance(request.json, dict):
            jobdesc = request.json

    jobres = createReservation(jobdesc)

    return json.dumps(jobres)


@app.route('/v2.0/checkReservation', methods=['GET'])
def api2_checkReservation():
    return json.dumps({"Ready": False})


@app.route('/v2.0/getReservationMetrics', methods=['GET'])
def api2_getReservationMetrics():
    return json.dumps({"Reservations": []})


@app.route('/v2.0/releaseReservation', methods=['DELETE'])
def api2_releaseReservation():
    return json.dumps({})
