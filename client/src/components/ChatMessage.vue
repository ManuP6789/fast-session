<template>
  <div v-if="messageType === 'user'" class="p-2 d-flex flex-row justify-content-end">
    <div class="message user-message">
      <p class="sender mb-1">{{ sender }}</p>
      {{ message }}
    </div>
    <div class="logo-circle user-circle d-flex">
      <span class="user-icon">{{ firstLetter }}</span>
    </div>
  </div>
  <div v-else class="p-2 d-flex flex-row align-self-start">
    <div class="logo-circle bot-circle d-flex">
      <img class="coach-icon" :src="coachLogo" alt="" />
    </div>
    <div class="message bot-message">
      <p class="sender mb-1">{{ sender }}</p>
      {{ message }}
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType, computed } from 'vue'
import coachLogo from '../assets/icons/image.png'

export default defineComponent({
  name: 'ChatMessage',
  props: {
    message: {
      type: String as PropType<string>,
      required: true
    },
    messageType: {
      type: String as PropType<string>,
      required: true
    },
    sender: {
      type: String as PropType<string>,
      required: true
    }
  },
  setup(props) {
    const firstLetter = computed(() => props.sender.charAt(0).toUpperCase())

    return {
      firstLetter
    }
  },
  data() {
    return {
      coachLogo
    }
  }
})
</script>

<style scoped>
.message {
  border-radius: 10px;
  padding: 5px 15px;
  max-width: 70%;
  word-wrap: break-word;
}
.user-message {
  background-color: rgb(6, 131, 118);
  color: white;
}
.bot-message {
  background-color: rgb(244, 244, 249);
  color: black;
}
.sender {
  font-weight: bold;
}
.logo-circle {
  height: 35px;
  width: 35px;
  border-radius: 50%;
}
.bot-circle {
  margin-right: 8px;
  background-color: #ff4f00;
}
.user-circle {
  margin-left: 8px;
  background-color: rgb(6, 131, 118);
}
.coach-icon {
  margin: auto;
  height: 24px;
  width: 24px;
  filter: brightness(0) invert(1);
}
.user-icon {
  margin: auto;
  height: 24px;
  width: 24px;
  align-items: center;
  text-align: center;
  color: white;
}
</style>
