<template>
  <Header />
  <RouterView />
</template>

<script setup>
import { RouterView } from 'vue-router'
</script>
import Header from './components/Header.vue' export default { name: 'App', components: { Header } }

<style>
#app {
  margin-top: 10px;
}
</style>
