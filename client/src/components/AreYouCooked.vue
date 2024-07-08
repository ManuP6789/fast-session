<template>
  <div class="container mt-5">
    <div class="page-header text-center">
      <h1>AWS Bedrock</h1>
      <hr />
    </div>
    <div class="chat-container card">
      <div ref="chatMessages" class="chat-messages card-body">
        <ChatMessage
          v-for="(message, index) in messages"
          :key="index"
          :message="message.text"
          :messageType="message.type"
        />
      </div>
      <div class="chat-input card-footer d-flex">
        <input
          type="text"
          v-model="newMessage"
          @keyup.enter="sendMessage"
          class="form-control me-2"
          placeholder="Type a message..."
        />
        <button @click="sendMessage" class="btn btn-primary">Send</button>
      </div>
    </div>
  </div>
</template>

<script>
import ChatMessage from './ChatMessage.vue'
import axios from 'axios'

export default {
  name: 'Cooked',
  components: {
    ChatMessage
  },
  data() {
    return {
      messages: [],
      newMessage: ''
    }
  },
  methods: {
    async sendMessage() {
      if (this.newMessage.trim() !== '') {
        this.messages.push({ text: this.newMessage, type: 'user' })
        const userMessage = this.newMessage
        this.newMessage = ''
        this.scrollToBottom()

        try {
          const response = await this.generateBotResponse(userMessage)
          this.messages.push({ text: response.generated_text, type: 'bot' })
        } catch (error) {
          console.error('Error generating bot response:', error)
        }
        this.scrollToBottom()
      }
    },
    async generateBotResponse(message) {
      const response = await axios.post('http://127.0.0.1:5000/generate', {
        input_text: message
      })
      return response.data
    },
    scrollToBottom() {
      this.$nextTick(() => {
        const messagesContainer = this.$refs.chatMessages
        const scrollHeight = messagesContainer.scrollHeight
        const clientHeight = messagesContainer.clientHeight
        const scrollTop = messagesContainer.scrollTop
        const distance = scrollHeight - clientHeight - scrollTop
        const duration = 300 // Adjust as needed

        let start = null

        const step = (timestamp) => {
          if (!start) start = timestamp
          const progress = timestamp - start
          const percentage = Math.min(progress / duration, 1)

          messagesContainer.scrollTop = scrollTop + distance * percentage

          if (progress < duration) {
            window.requestAnimationFrame(step)
          }
        }

        window.requestAnimationFrame(step)
      })
    }
  },
  mounted() {
    this.scrollToBottom() // Initial scroll to bottom
  }
}
</script>

<style scoped>
.chat-container {
  display: flex;
  flex-direction: column;
  height: 75vh;
  max-width: 600px;
  margin: 0 auto;
  border: 1px solid #ccc;
  border-radius: 10px;
  overflow: hidden;
}
.chat-messages {
  flex: 1;
  padding: 10px;
  overflow-y: scroll;
  background-color: #f9f9f9;
}
</style>
