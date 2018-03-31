import types from './types';

export const mutations = {
  [types.GET_TODO](state, { todos, error }) {
    state.todos = todos;
    state.error = error;
  },
  [types.CLEAR_TODO](state) {
    state.todos = [];
    state.error = '';
  },
  [types.CREATE_TODO](state, { content, todoId, error }) {
    state.todos.push({
      id: todoId,
      content,
      is_done: false,
    });
    state.error = error;
  },
};

export const state = {
  todos: [],
  error: '',
};
