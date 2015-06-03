from flask import Blueprint, request, json

from bqwm.schedulers import createReservation

api_v2_0 = Blueprint('api_v2_0', __name__)


@api_v2_0.route('/addManager', methods=['POST'])
def api_addManager():
    return json.dumps({})


@api_v2_0.route('/getConfigurationCost', methods=['POST'])
def api_getConfigurationCost():
    return json.dumps({"Costs": []})


@api_v2_0.route('/createReservation', methods=['POST'])
def api_createReservation():

    jobdesc = {}

    if request.headers['Content-Type'] == 'application/json':
        if isinstance(request.json, dict):
            jobdesc = request.json

    jobres = createReservation(jobdesc)

    return json.dumps(jobres)


@api_v2_0.route('/checkReservation', methods=['GET'])
def api_checkReservation():
    return json.dumps({"Ready": False})


@api_v2_0.route('/getReservationMetrics', methods=['GET'])
def api_getReservationMetrics():
    return json.dumps({"Reservations": []})


@api_v2_0.route('/releaseReservation', methods=['DELETE'])
def api_releaseReservation():
    return json.dumps({})
