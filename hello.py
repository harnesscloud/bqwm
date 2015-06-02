from flask import Flask, request, json
app = Flask(__name__)


@app.route('/createReservation', methods=['POST'])
def api_createReservation():
    if request.headers['Content-Type'] == 'application/json':
        configs = []
        try:
            configs = request.json["Configurations"]
        except:
            pass
    
        if len(configs) > 0:
            return json.dumps(configs[0])

    return "no config"

if __name__ == '__main__':
    app.run()
