import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

export default createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: Home,
    },
    {
      path: '/login',
      component: () => import('../views/Login.vue'),
    },
    {
      path: '/about',
      component: () => import('../views/About.vue'),
    },
    {
      path: '/contact',
      component: () => import('../views/Contact.vue'),
    },
    {
      path: '/register',
      component: () => import('../views/Register.vue'),
    },
    {
      path: '/profile',
      component: () => import('../views/Profile.vue'),
    },
    {
      path: '/leaderboard/:sessionId',
      component: () => import('../views/Leaderboard.vue'),
    },
    {
      path: '/create-session',
      component: () => import('../views/QuizSession.vue'),
    }
  ],
})
