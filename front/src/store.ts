import axios from 'axios';
import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    apiUrl: process.env.VUE_APP_API_URL || 'http://localhost:8080',
    quote: {},

  },
  mutations: {
    setCurrentQuote(currentState, quote) {
      currentState.quote = quote;
    },
  },
  actions: {
    async getRandomQuote(context) {
      const response = await axios.get(`${context.state.apiUrl}/quotes/random`);
      context.commit('setCurrentQuote', response.data);
    },
  },
});
