import Vue from 'vue';
import Vuex from 'vuex';
import todo from '@/store/todo';

Vue.use(Vuex);

const store = new Vuex.Store({
  modules: {
    todo,
  },
  strict: true,
});

export default store;
