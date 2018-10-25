import axios from 'axios';
import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    apiUrl: 'http://localhost:8080',
    quote: {},

  },
  mutations: {
    setCurrentQuote(currentState, quote) {
      currentState.quote = quote;
    },
  },
  actions: {
    async getRandomQuote(context) {
      const response = await axios.get(`http://localhost:8080/quotes/random`);
      context.commit('setCurrentQuote', response.data);
    },
  },
});
