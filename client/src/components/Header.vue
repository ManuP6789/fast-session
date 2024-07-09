<template>
  <header class="bg-light p-3">
    <div class="container d-flex flex-row justify-content-between align-items-center">
      <div class="d-flex align-items-center flex-row">
        <img :src="logoSrc" alt="Logo" class="mr-3" style="height: 40px" />
        <h1 class="h4 mb-0">{{ title }}</h1>
      </div>
      <nav class="mt-3">
        <ul class="list-inline">
          <li class="list-inline-item">
            <router-link to="/" class="text-decoration-none">Home</router-link>
          </li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script setup lang="ts"></script>

<style scoped></style>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'HeaderSection',
  props: {
    logoSrc: String,
    title: String
  }
})
</script>
