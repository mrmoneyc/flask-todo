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


@api.route('/todo')
@api.route('/todo/<int:todo_id>')
class TodoResource(Resource):
    def get(self, todo_id=None):
        if not todo_id:
            return 'Get all todos'
        else:
            return 'Get todo by id: %d' % todo_id

    def post(self):
        return 'Create todo'

    def put(self, todo_id=None):
        if not todo_id:
            return 'Todo ID is required'
        else:
            return 'Update todo by id: %d' % todo_id

    def delete(self, todo_id=None):
        if not todo_id:
            return 'Todo ID is required'
        else:
            return 'Delete todo by id: %d' % todo_id


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
