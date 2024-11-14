import authService from '@/services/auth.service';
import { AuthState, ILogin, IUserRegister } from '@/types/auth';
import { Module, State } from 'vuex';

const state: AuthState = {
  isAuthenticated: false
};

const authModule: Module<AuthState, State> = {
  namespaced: true,
  state,
  mutations: {
    logIn(state: AuthState, isAuthenticated: boolean) {
      state.isAuthenticated = isAuthenticated;
    },
    logOut(state: AuthState, isAuthenticated: boolean) {
      state.isAuthenticated = isAuthenticated;
    }
  },
  actions: {
    async login( { commit }, params: ILogin ) {
      const status = await authService.login(params)
      commit("logIn", status)
    },

    logout( { commit }) {
      commit('logOut', false);
    },

    async register(params: IUserRegister) {
      return await authService.register(params)
    }
  },
  getters: {
    isAuthenticated(state: State): boolean {
      return !!state.isAuthenticated;
    },
  },
};

export default authModule;
