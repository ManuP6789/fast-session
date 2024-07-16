<template>
  <router-view />
</template>

<script lang="ts" setup>
import { RouterView } from 'vue-router'
</script>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'App',
  components: {
    RouterView
  }
})
</script>

<style>
html,
body,
#app {
  height: 100%;
  width: 100%;
  color: rgb(65, 59, 81);
  font-family: Arial, Helvetica, sans-serif;
}
</style>
