import Vue from 'vue';
import BootstrapVue from 'bootstrap-vue';
import VueTouch from 'vue-touch';
import App from './App.vue';
import store from './store';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

Vue.config.productionTip = false;
Vue.use(BootstrapVue);
Vue.use(VueTouch, {name: 'v-touch'});

new Vue({
  store,
  render: (h) => h(App),
}).$mount('#app');
