<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container">
        <a class="navbar-brand" href="#">QuizApp</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto">
            <li v-if="!isAuthenticated" class="nav-item">
              <router-link to="/login" class="nav-link">Login</router-link>
            </li>
            <li v-if="!isAuthenticated" class="nav-item">
              <router-link to="/register" class="nav-link">Register</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/create-session" class="nav-link">Create Session</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/leaderboard/123" class="nav-link">Leaderboard</router-link>
            </li>
            <li v-if="isAuthenticated">
              <a href="" class="nav-link" @click="logout">Logout</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </template>
  
  <script lang="ts">
  import { defineComponent, computed  } from 'vue';
  import { useStore } from 'vuex';
  import { useRouter } from 'vue-router';
  
  export default defineComponent({
    name: 'NavigationMenu',
    setup() {
      const store = useStore();
      const router = useRouter();
      const isAuthenticated = computed(() => store.getters['authModule/isAuthenticated']);

      const logout = () => {
        store.dispatch('authModule/logout');
        router.push('/');
      };

      return {
        isAuthenticated,
        logout,
      };

    }
  });
  </script>
  
  <style scoped>
  .navbar {
    margin-bottom: 20px;
  }
  </style>
  