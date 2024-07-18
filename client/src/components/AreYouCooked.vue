<template>
  <div class="activity-container d-flex h-100">
    <HeaderSection :logoSrc="appLogo" :name="userInfo.name" />
    <UserModal v-if="modalShown" @submit="saveUserInfo" @close="modalShown = false" />
    <div class="d-flex flex-column w-100">
      <div class="d-flex p-3 justify-content-between w-100">
        <div class="pr-3"><h5>Networking: The basics</h5></div>
        <div @click="restartChat" class="d-flex flex-row">
          <img :src="refresh" class="icon" />
          <p>Start New Chat</p>
        </div>
      </div>
      <div class="chat-container d-flex flex-column justify-content-between h-100">
        <div ref="chatMessages" class="chat-messages card-body">
          <ChatMessage
            v-for="(message, index) in messages"
            :key="index"
            :message="message.text"
            :messageType="message.type"
            :sender="message.sender"
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
        <button v-if="showFinishActivityButton" @click="showSurvey" class="btn btn-secondary">
          Finish Activity
        </button>
      </div>
    </div>
    <div class="d-flex justifiy-content-center align-items-center">
      <img class="icon expand" :src="isSidebarOpen ? close : expand" @click="closeSuggestionsBar" />
    </div>

    <SuggestionsBar ref="suggestionsBarRef" :suggestions="suggestions" />
    <SurveyModal v-if="showSurveyModal" :firstQuestion="userInfo.goal" @close="closeSurvey" />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, nextTick, computed } from 'vue'
import HeaderSection from './Header.vue'
import ChatMessage from './ChatMessage.vue'
import UserModal from './UserModal.vue'
import SurveyModal from './SurveyModal.vue'
import SuggestionsBar, { SuggestionsBarInstance } from './SuggestionsBar.vue'
import axios from 'axios'
import logoImg from '../assets/Coach_fulllockup_mini.png'
import refresh from '../assets/icons/restart_alt_24dp_434343_FILL0_wght400_GRAD0_opsz24.png'
import expand from '../assets/icons/arrow_circle_left_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.png'
import close from '../assets/icons/arrow_circle_right_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.png'

export default defineComponent({
  name: 'AreYouCooked',
  components: {
    ChatMessage,
    HeaderSection,
    UserModal,
    SuggestionsBar,
    SurveyModal
  },
  data() {
    return {
      close,
      expand,
      refresh,
      appLogo: logoImg,
      messages: [
        {
          text: "Welcome to our Networking Skills activity! Let's unlock the potential of your connections and advance your career. Ready to start?",
          type: 'bot',
          sender: 'Coach'
        }
      ] as Array<{ text: string; type: string; sender: string }>,
      newMessage: '' as string,
      userInfo: {
        goal: '' as string,
        field: '' as string,
        stage: '' as string,
        name: '' as string
      },
      modalShown: true as boolean,
      suggestions: [] as string[],
      showSurveyModal: false,
      showFinishActivityButton: false
    }
  },
  methods: {
    async sendMessage() {
      if (this.newMessage.trim() !== '') {
        this.messages.push({ text: this.newMessage, type: 'user', sender: this.userInfo.name })
        let userMessage = this.newMessage
        this.newMessage = ''
        this.scrollToBottom()

        try {
          const response = await this.generateBotResponse(userMessage)
          this.messages.push({ text: response.generated_text, type: 'bot', sender: 'Coach' })

          // Assuming generateSuggestionResponse takes the generated_text as input
          if (this.isSidebarOpen) {
            let sugResponse
            try {
              sugResponse = await Promise.race([
                this.generateSuggestionResponse(response.generated_text),
                new Promise((resolve, reject) => {
                  setTimeout(() => reject(new Error('Timeout')), 4000) // 2 second timeout
                })
              ])
              sugResponse = sugResponse || []
            } catch (error) {
              console.error('Suggestion generation timed out:', error)
              sugResponse = { suggestions: [] } // Handle timeout gracefully
              sugResponse = []
            }
            if (typeof sugResponse === 'string') {
              // Case 1: sugResponse is a string suggestion
              this.updateSuggestions(sugResponse)
            } else if (
              sugResponse &&
              sugResponse.generated_text &&
              typeof sugResponse.generated_text.text === 'string'
            ) {
              // Case 2: sugResponse is an object with a generated_text.text property
              this.updateSuggestions(sugResponse)
            } else {
              console.error('Invalid response format from generateSuggestionResponse:', sugResponse)
              // Handle unexpected response format gracefully
            }
          }
        } catch (error) {
          console.error('Error generating bot response:', error)
        }
        if (this.messages.length > 3) {
          this.showFinishActivityButton = true
        }
        this.scrollToBottom()
      }
    },
    async generateBotResponse(message: String) {
      const response = await axios.post('http://127.0.0.1:5000/generate', {
        input_text: message,
        coach_text_history: this.getLastBotMessage(),
        user_text_history: this.getLastUserMessage(),
        user_goals: this.userInfo.goal,
        user_major: this.userInfo.field,
        user_grade: this.userInfo.stage
      })
      return response.data
    },
    async generateSuggestionResponse(suggestion: String) {
      const response = await axios.post('http://127.0.0.1:5000/generateSuggestion', {
        coach_text_history: suggestion,
        user_text_history: this.getLastUserMessage(),
        user_goals: this.userInfo.goal,
        user_major: this.userInfo.field,
        user_grade: this.userInfo.stage
      })
      return response.data
    },
    getLastBotMessage() {
      const lastBotMessage = this.messages
        .filter((message) => message.sender === 'Coach')
        .slice(-1)[0]
      return lastBotMessage ? lastBotMessage.text : ''
    },
    getLastUserMessage() {
      const lastUserMessage = this.messages
        .filter((message) => message.sender === this.userInfo.name)
        .slice(-1)[0]
      return lastUserMessage ? lastUserMessage.text : ''
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
    saveUserInfo(userInfo: { goal: string; field: string; stage: string; name: string }) {
      this.userInfo = userInfo
      this.modalShown = false
    },
    restartChat() {
      this.messages = [
        {
          text: "Welcome to our Networking Skills activity! Let's unlock the potential of your connections and advance your career. Ready to start?",
          type: 'bot',
          sender: 'Coach'
        }
      ]
      this.newMessage = ''
      this.scrollToBottom()
    },
    updateSuggestions(newSuggestions: string | { generated_text: { text: string } }) {
      if (typeof newSuggestions === 'string') {
        this.suggestions.push(newSuggestions) // String case
      } else if (
        newSuggestions &&
        newSuggestions.generated_text &&
        typeof newSuggestions.generated_text.text === 'string'
      ) {
        this.suggestions.push(newSuggestions.generated_text.text) // Object case with generated_text.text property
      } else {
        console.error('Invalid response format from generateSuggestionResponse:', newSuggestions)
        // Handle unexpected response format gracefully
      }
    },
    showSurvey() {
      this.showSurveyModal = true
    },
    closeSurvey() {
      this.showSurveyModal = false
    }
  },
  mounted() {
    this.scrollToBottom() // Initial scroll to bottom
  },
  setup() {
    const suggestionsBarRef = ref<SuggestionsBarInstance | null>(null)
    const isSidebarOpen = computed(() => suggestionsBarRef.value?.isSidebarOpen ?? false)

    const closeSuggestionsBar = () => {
      if (suggestionsBarRef.value) {
        suggestionsBarRef.value.toggleSidebar()
      }
    }

    return {
      isSidebarOpen,
      suggestionsBarRef,
      closeSuggestionsBar
    }
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

.chat-input ::placeholder {
  color: #9f9c9cb8; /* Light gray color */
}
#p {
  font-size: 10px;
}
.icon {
  height: 24px;
  width: 24px;
  margin-right: 8px;
}
.btn {
  background-color: rgb(6, 131, 118);
}
.btn-primary:hover {
  background-color: rgb(126, 8, 139);
}
.btn-primary:active {
  background-color: rgb(126, 8, 129);
}
.button-bar {
  width: 20px;
  height: 10px;
  position: relative;
}
</style>
