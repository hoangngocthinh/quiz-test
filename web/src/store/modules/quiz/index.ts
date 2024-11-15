import { Module, State } from 'vuex';

const state: AuthState = {
  isAuthenticated: false
};

const quizModule: Module<AuthState, State> = {
  namespaced: true,
  state,
  mutations: {
  },
  actions: {
  },
  getters: {
  },
};

export default quizModule;
