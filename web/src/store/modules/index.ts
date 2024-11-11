// src/store/index.ts
import { createStore } from 'vuex';
import userModule, { UserState } from './modules/user';

export interface State {
  isAuthenticated: boolean;
  user: UserState;
}

export default createStore<State>({
  state: {
    isAuthenticated: !!localStorage.getItem('access_token'),
  },
  mutations: {
    login(state) {
      state.isAuthenticated = true;
    },
    logout(state) {
      state.isAuthenticated = false;
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
    },
  },
  actions: {
    login({ commit }) {
      commit('login');
    },
    logout({ commit }) {
      commit('logout');
    },
  },
  getters: {
    isAuthenticated: (state) => state.isAuthenticated,
  },
  modules: {
    user: userModule, // Thêm module user
  },
});
