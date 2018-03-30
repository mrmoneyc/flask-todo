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
};

export const state = {
  todos: [],
  error: '',
};
