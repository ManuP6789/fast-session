<template>
  <HeaderSection :title="appTitle" :logoSrc="appLogo" />
  <router-view />
</template>

<script lang="ts" setup>
import { RouterView } from 'vue-router'
</script>

<script lang="ts">
import { defineComponent } from 'vue'
import HeaderSection from './components/Header.vue' // Import your Header component here

// Define props for Header component
const appTitle = 'Coach'
const appLogo = './src/assets/596a68bc6e28303e5a2badb2516d56eb.png'

export default defineComponent({
  name: 'App',
  components: {
    RouterView,
    HeaderSection
  }
})
</script>

<style>
#app {
  margin-top: 10px;
}
</style>
