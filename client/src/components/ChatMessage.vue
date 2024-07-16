<template>
  <div
    :class="['p-2', 'd-flex', messageType == 'user' ? 'justify-content-end' : 'align-self-start']"
  >
    <div :class="['message', messageType === 'user' ? 'user-message' : 'bot-message']">
      {{ message }}
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue'

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
  background-color: #007bff;
  color: white;
}

.bot-message {
  background-color: rgb(244, 244, 249);
  color: black;
}
</style>
