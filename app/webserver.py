from bottle import Bottle, HTTPResponse
import os

VERSION='0.0.1'
BOTTLEIP='0.0.0.0'
BOTTLEPORT='8500'

APP = Bottle(__name__)


@APP.route('/', method=['OPTIONS', 'GET'])
def index():
    try:
        apname = os.environ['NAME']
        body= {'version': VERSION, 'apname': apname}
        response = HTTPResponse(status=200, body=body)
        return response
    except Exception as err:
        print(err)
        body={'version': VERSION, 'err': err}
        response = HTTPResponse(status=400, body=body)
        return response



if __name__ == '__main__':
    try:
        SERVER = APP.run(host=BOTTLEIP, port=BOTTLEPORT, debug=True)
    except KeyboardInterrupt:
        pass
        print('exiting....')
        SERVER.stop()
