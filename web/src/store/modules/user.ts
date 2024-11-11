import { Module } from 'vuex';
import { State } from '../index';

export interface UserState {
  id: number | null;
  name: string;
}

const userModule: Module<UserState, State> = {
  state: {
    id: null,
    name: '',
  },
  mutations: {
    setUser(state, user: UserState) {
      state.id = user.id;
      state.name = user.name;
    },
    clearUser(state) {
      state.id = null;
      state.name = '';
    },
  },
  actions: {
    setUser({ commit }, user: UserState) {
      commit('setUser', user);
    },
    clearUser({ commit }) {
      commit('clearUser');
    },
  },
  getters: {
    user: (state) => state,
  },
};

export default userModule;
