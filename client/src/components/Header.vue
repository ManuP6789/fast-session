<template>
  <div class="header d-flex flex-column justify-content-between">
    <div class="p-4">
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
    <div class="name">
      <h8 class="p-2">Manuel</h8>
    </div>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.header {
  background-color: rgb(244, 244, 249);
  width: 20%;
}
.name {
  margin: 1px solid #ccc;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>

<script lang="ts">
import { defineComponent, PropType } from 'vue'

export default defineComponent({
  name: 'HeaderSection',
  props: {
    title: {
      type: String as PropType<string>,
      required: true
    },
    logoSrc: {
      type: String as PropType<string>,
      required: true
    }
  }
})
</script>
