<template>
  <div class="activity-container d-flex h-100">
    <HeaderSection :logoSrc="appLogo" :name="userInfo.name" />
    <UserModal v-if="modalShown" @submit="saveUserInfo" @close="modalShown = false" />
    <div class="d-flex flex-column w-100">
      <div class="d-flex p-3 justify-content-between w-100">
        <div class="pr-3"><h5>Networking: The basics</h5></div>
        <div><p>Start New Chat</p></div>
      </div>
      <div class="chat-container d-flex flex-column justify-content-between h-100">
        <div ref="chatMessages" class="chat-messages card-body">
          <ChatMessage
            v-for="(message, index) in messages"
            :key="index"
            :message="message.text"
            :messageType="message.type"
          />
        </div>
        <div class="chat-input card-footer d-flex m-4">
          <input
            type="text"
            v-model="newMessage"
            @keyup.enter="sendMessage"
            class="form-control me-2"
            placeholder="Message Coach"
          />
          <button @click="sendMessage" class="btn btn-primary">Send</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, nextTick } from 'vue'
import HeaderSection from './Header.vue'
import ChatMessage from './ChatMessage.vue'
import UserModal from './UserModal.vue'
import axios from 'axios'
import logoImg from '../assets/Coach_fulllockup_mini.png'

export default defineComponent({
  name: 'AreYouCooked',
  components: {
    ChatMessage,
    HeaderSection,
    UserModal
  },
  data() {
    return {
      appLogo: logoImg,
      messages: [
        {
          text: "Welcome to our Networking Skills activity! Let's unlock the potential of your connections and advance your career. Ready to start?",
          type: 'bot'
        }
      ] as Array<{ text: string; type: string }>,
      newMessage: '' as string,
      userInfo: {
        goal: '' as string,
        field: '' as string,
        stage: '' as string,
        name: '' as string
      },
      modalShown: true as boolean
    }
  },
  methods: {
    async sendMessage() {
      if (this.newMessage.trim() !== '') {
        this.messages.push({ text: this.newMessage, type: 'user' })
        let userMessage = this.newMessage
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
    async generateBotResponse(message: String) {
      const response = await axios.post('http://127.0.0.1:5000/generate', {
        input_text: message
      })
      return response.data
    },
    scrollToBottom() {
      nextTick(() => {
        const messagesContainer = this.$refs.chatMessages as HTMLELement
        const scrollHeight = messagesContainer.scrollHeight
        const clientHeight = messagesContainer.clientHeight
        const scrollTop = messagesContainer.scrollTop
        const distance = scrollHeight - clientHeight - scrollTop
        const duration = 300 // Adjust as needed

        let start: number | null = null

        const step = (timestamp: number) => {
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
    },
    saveUserInfo(userInfo: { goal: string; field: string; stage: string }) {
      this.userInfo = userInfo
      this.modalShown = false
    }
  },
  mounted() {
    this.scrollToBottom() // Initial scroll to bottom
  }
})
</script>

<style scoped>
.chat-container {
  margin: 0 auto;
  overflow: hidden;
  width: 800px;
}
.chat-messages {
  flex: 1;
  padding: 10px;
  overflow-y: scroll;
}
.chat-input {
  background-color: white;
}
#p {
  font-size: 10px;
}
</style>
