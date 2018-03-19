# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_restplus import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import expression
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://todo:todo@127.0.0.1:3306/todo?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db = SQLAlchemy(app)


# == Data Schemas ==
class TodoSchema(Schema):
    id = fields.Int(dump_only=True)
    content = fields.Str()
    is_done = fields.Bool(missing=False)


todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)


# == DB Models ==
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    is_done = db.Column(db.Boolean, server_default=expression.false(), default=False)

    def __repr__(self):
        return '<Todo %r>' % self.content


# == API Handlers ==
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
        todo_list = None

        if not todo_id:
            todo_list, _ = todos_schema.dump(Todo.query.all())
        else:
            todo_list, _ = todo_schema.dump(Todo.query.filter_by(id=todo_id).first())

        resp_body = {
                'result': todo_list
        }
        return resp_body

    def post(self):
        req_body = request.get_json()
        if not req_body:
            return {'message': 'No todo data provided'}, 400

        try:
            data, _ = todo_schema.load(req_body)
        except ValidationError as err:
            return err.messages, 422

        content = data['content']
        is_done = data['is_done']

        todo = Todo(content=content, is_done=is_done)
        db.session.add(todo)
        db.session.commit()
        return todo.id, 201

    def put(self, todo_id=None):
        if not todo_id:
            return {'message': 'Todo ID is required'}, 400

        req_body = request.get_json()
        if not req_body:
            return {'message': 'No todo data provided'}, 400

        try:
            data, _ = todo_schema.load(req_body)
        except ValidationError as err:
            return err.messages, 422

        content = data['content']
        is_done = data['is_done']

        todo = Todo.query.filter_by(id=todo_id).first()
        if not todo:
            return {'message': 'Todo not found'}, 404

        setattr(todo, 'content', content)
        setattr(todo, 'is_done', is_done)
        db.session.commit()
        return todo.id


    def delete(self, todo_id=None):
        if not todo_id:
            return 'Todo ID is required'
        else:
            return 'Delete todo by id: %d' % todo_id


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
