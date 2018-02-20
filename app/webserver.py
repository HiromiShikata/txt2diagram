from bottle import Bottle, HTTPResponse, request
import os
import requests

VERSION='0.0.1'
BOTTLEIP='0.0.0.0'
BOTTLEPORT='8500'

APP = Bottle(__name__)


@APP.route('/')
def index():
    try:
        url=request.query.url
        print(url)
        apname = os.environ['NAME']
        r = requests.get(url)
        print(r.text)
        body= {'version': VERSION, 'apname': apname, 'url': url, 'text': r.text}

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
