// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import Meta from 'vue-meta';
import Buefy from 'buefy';
import 'mdi/css/materialdesignicons.min.css';
import 'buefy/lib/buefy.css';

import App from './App';
import store from './store';

Vue.use(Buefy);
Vue.use(Meta);
Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>',
  store,
});
