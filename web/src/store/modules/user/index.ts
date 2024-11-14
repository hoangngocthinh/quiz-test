import userService from '@/services/user.service';
import { IUser, UserState } from '@/types/user';
import { Module, State } from 'vuex';

const state: UserState = {
  user: {
    id: null,
    username: '',
    email: '',
    first_name: '',
    last_name: ''
  }
};

const userModule: Module<UserState, State> = {
  namespaced: true,
  state,
  mutations: {
    setUser(state: State, user: IUser) {
      state.user = user;
    },
  },
  actions: {
    async getMyProfile( { commit }) {
      const user = await userService.getMyProfile()
      commit("setUser", user)
    }
  },
};

export default userModule;
