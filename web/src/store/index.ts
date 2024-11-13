import { InjectionKey } from 'vue'
import { createStore, State, Store, useStore as baseUseStore } from 'vuex';
import authModule from '@/store/modules/auth';
import userModule from './modules/user';


export const store = createStore<State>({
  modules: {
    authModule, 
    userModule,
  },
});

export const key: InjectionKey<Store<State>> = Symbol()

export function useStore () {
  return baseUseStore(key)
}
