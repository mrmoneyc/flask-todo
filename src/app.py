# -*- coding: utf-8 -*-
import json
from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
@api.route('/hello/<string:username>')
class HelloResource(Resource):
    def get(self, username=None):
        if not username:
            username = 'World!'

        resp_body = {
                'Hello': username
        }

        return resp_body


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
