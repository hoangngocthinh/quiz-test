import userService from '@/services/user.service';
import { UserState } from '@/types/user';
import { Module, State } from 'vuex';

const state: UserState = {
  id: null,
  username: "",
  email: "",
  first_name: "",
  last_name: "",
  password: "",
  password1: "",
};

const userModule: Module<UserState, State> = {
  namespaced: true,
  state,
  mutations: {
    setUser(state: State, user: UserState) {
      state.id = user.id;
      state.username = user.username;
      state.email = user.email;
      state.first_name = user.first_name;
      state.last_name = user.last_name;
    },
  },
  actions: {
    updateUser( { commit }, user: UserState) {
      commit('setUser', user);
    },
    async getMyProfile( { commit }) {
      const user = await userService.getMyProfile()
      commit("setUser", user)
    }
  },
};

export default userModule;
