# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_restplus import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import expression

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://todo:todo@127.0.0.1:3306/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    is_done = db.Column(db.Boolean, server_default=expression.false(), default=False)

    def __repr__(self):
        return '<Todo %r>' % self.content


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
        todo_list = []

        if not todo_id:
            todo_list = Todo.query.all()
        else:
            todo_list = Todo.query.filter_by(id=todo_id).first()

        resp_body = {
                'result': todo_list
        }
        return resp_body

    def post(self):
        req_body = request.get_json()
        content = req_body['content']
        is_done = req_body['is_done']

        todo = Todo(content=content, is_done=is_done)
        db.session.add(todo)
        db.session.commit()
        return todo.id

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
