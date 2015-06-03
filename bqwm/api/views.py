from flask import Blueprint, request, json

from bqwm.schedulers import createReservation

api = Blueprint('api', __name__)


@api.route('/addManager', methods=['POST'])
def api2_addManager():
    return json.dumps({})


@api.route('/getConfigurationCost', methods=['POST'])
def api2_getConfigurationCost():
    return json.dumps({"Costs": []})


@api.route('/createReservation', methods=['POST'])
def api2_createReservation():

    jobdesc = {}

    if request.headers['Content-Type'] == 'application/json':
        if isinstance(request.json, dict):
            jobdesc = request.json

    jobres = createReservation(jobdesc)

    return json.dumps(jobres)


@api.route('/checkReservation', methods=['GET'])
def api2_checkReservation():
    return json.dumps({"Ready": False})


@api.route('/getReservationMetrics', methods=['GET'])
def api2_getReservationMetrics():
    return json.dumps({"Reservations": []})


@api.route('/releaseReservation', methods=['DELETE'])
def api2_releaseReservation():
    return json.dumps({})
