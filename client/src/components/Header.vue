<template>
  <div class="header d-flex flex-column justify-content-between">
    <div class="d-flex flex-column p-4 h-100">
      <div class="d-flex align-items-center flex-row">
        <img :src="logoSrc" alt="Logo" class="logo mr-3" style="height: 65px" />
      </div>
      <div class="d-flex flex-column justify-content-between h-100">
        <nav class="mt-3">
          <ul class="list">
            <li class="list-inline-item">
              <router-link to="/" class="text-decoration-none">Home</router-link>
            </li>
            <li class="list-inline-item">
              <router-link to="/" class="text-decoration-none">Find Activities</router-link>
            </li>
            <li class="list-inline-item">
              <router-link to="/" class="text-decoration-none">History</router-link>
            </li>
          </ul>
        </nav>
        <nav class="mt-3">
          <ul class="list">
            <li class="list-inline-item">
              <router-link to="/" class="text-decoration-none">Feedback</router-link>
            </li>
            <li class="list-inline-item">
              <router-link to="/" class="text-decoration-none">Help</router-link>
            </li>
            <li class="list-inline-item">
              <router-link to="/" class="text-decoration-none">About</router-link>
            </li>
          </ul>
        </nav>
      </div>
    </div>
    <div class="name">
      <h8 class="p-2">{{ name }}</h8>
    </div>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.header {
  background-color: rgb(244, 244, 249);
  border-right: 1px solid #ccc;
  height: 100%;
  width: 20%;
}
.name {
  border-top: 1px solid #ccc;
  display: flex;
  justify-content: center;
  align-items: center;
}
.list {
  padding: 0;
  margin: 0;
  list-style: none;
}
.list li {
  display: block;
  width: 100%;
  padding: 10px 0;
}
</style>

<script lang="ts">
import { defineComponent, PropType } from 'vue'

export default defineComponent({
  name: 'HeaderSection',
  props: {
    logoSrc: {
      type: String as PropType<string>,
      required: true
    },
    name: {
      type: String as PropType<string>,
      required: true
    }
  }
})
</script>
