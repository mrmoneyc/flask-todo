/* eslint no-console: ["error", { allow: ["dir", "warn", "error"] }] */
import { Toast } from 'buefy';
import types from './types';
import apiTodo from '../../api/todo';

const actionGetTodos = ({ commit }) => {
  apiTodo.getTodos((todos, error) => {
    if (error) {
      Toast.open({
        duration: 3000,
        message: error,
        type: 'is-danger',
      });
    }

    commit(types.GET_TODO, { todos, error });
  });
};

const actionClearTodos = ({ commit }) => {
  commit(types.CLEAR_TODO);
};

const actionCreateTodo = ({ commit }, content) => {
  apiTodo.createTodo(content, (todoId, error) => {
    commit(types.CREATE_TODO, { content, todoId, error });
  });
};

export default {
  actionGetTodos,
  actionClearTodos,
  actionCreateTodo,
};
