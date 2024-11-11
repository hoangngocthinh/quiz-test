<script setup lang="ts">
</script>

<template>
  <NavigationMenu />
  <main>
    <router-view />
  </main>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import NavigationMenu from './components/NavigationMenu.vue'

export default defineComponent({
  components: {
    NavigationMenu,
  },
})
</script>

<style lang="scss">
@use "@/styles/style.global.scss";
</style>
