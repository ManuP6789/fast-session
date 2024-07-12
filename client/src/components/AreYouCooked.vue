<template>
  <div class="container mt-5">
    <!-- Modal -->
    <div v-if="modalShown" class="modal-backdrop"></div>
    <div v-if="modalShown" class="modal" tabindex="-1" ref="userModal">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Activity Information</h5>
          </div>
          <div class="modal-body">
            <div><h6>Networking: The basics</h6></div>
            <form @submit.prevent="saveUserInfo">
              <div class="mb-3">
                <label for="goal" class="form-label"
                  >What are you hoping to gain from this activity?</label
                >
                <input
                  type="text"
                  class="form-control"
                  id="goal"
                  v-model="userInfo.goal"
                  required
                />
              </div>
              <div class="mb-3">
                <label for="field" class="form-label"
                  >What area of study or field are you interested in?</label
                >
                <input
                  type="text"
                  class="form-control"
                  id="field"
                  v-model="userInfo.field"
                  required
                />
              </div>
              <div class="mb-3">
                <label for="stage" class="form-label"
                  >Are you a high school or college student?</label
                >
                <input
                  type="text"
                  class="form-control"
                  id="stage"
                  v-model="userInfo.stage"
                  required
                />
              </div>
              <button type="submit" class="btn btn-primary">Submit</button>
            </form>
          </div>
        </div>
      </div>
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
  name: 'AreYouCooked',
  components: {
    ChatMessage
  },
  data() {
    return {
      messages: [
        {
          text: "Welcome to our Networking Skills activity! Let's unlock the potential of your connections and advance your career. Ready to start?",
          type: 'bot'
        }
      ],
      newMessage: '',
      userInfo: {
        goal: '',
        email: '',
        stage: ''
      },
      modalShown: true
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
          // if (this.messages.length === 2) {
          //   userMessage += `, I want to learn more about networking, I am a computer science major in college.`
          // }
          // console.log('this is userMessage:' + userMessage) 
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
    },
    saveUserInfo() {
      this.modalShown = false
      this.$refs.userModal.style.display = 'none'
    }
  },
  mounted() {
    this.$refs.userModal.style.display = 'block'
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
.modal {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1050;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  z-index: 1040;
}
.modal-dialog {
  position: relative;
}
.modal-content {
  padding: 20px;
}
</style>
