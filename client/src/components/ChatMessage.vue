<template>
  <div
    :class="['p-2', 'd-flex', messageType == 'user' ? 'justify-content-end' : 'align-self-start']"
  >
    <div :class="['message', messageType === 'user' ? 'user-message' : 'bot-message']">
      {{ message }}
    </div>
  </div>
</template>

<script>
export default {
  props: {
    message: {
      type: String,
      required: true
    },
    messageType: {
      type: String,
      required: true // 'user' or 'bot'
    }
  }
}
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
  background-color: #e0e0e0;
  color: black;
}
</style>
