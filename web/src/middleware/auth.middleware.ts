import { Store } from 'vuex';
import { Router } from 'vue-router';

export default async function authMiddleware(to: Router, from: Router, next: Function) {
  const store = Store();

  if (store.getters['authModule/isAuthenticated']) {
    return next();
  }

  const accessToken = localStorage.getItem('access_token');
  if (accessToken) {
    try {
      await store.dispatch('authModule/refreshToken');
      await store.dispatch('authModule/getUserMe');
      return next();
    } catch (error) {
      console.error('Token refresh failed', error);
      return next('/login');
    }
  }
  return next('/login');
}
