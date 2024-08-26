<template>
  <div class="modal" tabindex="-1" role="dialog" style="display: block">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Survey</h5>
        </div>
        <div class="modal-body flex-d align-items-center">
          <div
            v-for="(question, index) in questions"
            :key="index"
            class="survey-question d-flex align-items-center justify-content-center"
          >
            <div class="px-2 d-flex flex-column w-75">
              <label :for="'slider' + index">{{ question.text }}</label>
              <div class="flex-d align-items-center">
                <input
                  v-if="question.type === 'slider'"
                  class="slider"
                  type="range"
                  :id="'slider' + index"
                  v-model="responses[index]"
                  :min="1"
                  :max="5"
                />
                <span class="slider-value pl-1" v-if="question.type === 'slider'"
                  >Value: {{ responses[index] }}</span
                >
                <input
                  v-if="question.type === 'text'"
                  class="text-input w-100"
                  type="text"
                  :id="'text' + index"
                  v-model="responses[index]"
                  placeholder="Type your answer here"
                />
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-primary" @click="submitSurvey">Submit</button>
          <button type="button" class="btn btn-secondary" @click="$emit('close')">Close</button>
        </div>
      </div>
    </div>
    <AchievementModal v-if="showAchievement" @close="handleAchievementClose" />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, PropType, computed } from 'vue'
import AchievementModal from './AchievementModal.vue'

export default defineComponent({
  name: 'SurveyModal',
  props: {
    firstQuestion: {
      type: String,
      required: true
    }
  },
  components: {
    AchievementModal
  },
  setup(props, { emit }) {
    const firstQuestion = computed(() => props.firstQuestion)
    const questions = ref([
      { text: 'Rate your experience:', type: 'slider' },
      {
        text: `How do you think this activity helped you reach this goal: ${props.firstQuestion}`,
        type: 'slider'
      },
      { text: 'What did you like most?', type: 'text' },
      { text: 'How can we improve?', type: 'text' }
    ])
    const showAchievement = ref(false)
    const responses = ref(questions.value.map((question) => (question.type === 'slider' ? 3 : '')))

    const submitSurvey = () => {
      console.log('Survey responses:', responses.value)
      showAchievement.value = true

      //   emit('close')
    }

    const handleAchievementClose = () => {
      showAchievement.value = false
      emit('close')
    }

    return {
      firstQuestion,
      questions,
      responses,
      submitSurvey,
      showAchievement,
      handleAchievementClose
    }
  }
})
</script>

<style scoped>
.modal {
  background: rgba(0, 0, 0, 0.5);
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1050;
  overflow: hidden;
}
.modal-dialog {
  margin: 10% auto;
}
.slider {
  width: 70%; /* Ensure the slider takes up the available width */
  background-color: rgb(6, 131, 118);
}
.slider-value {
  margin-left: 10px; /* Add some spacing between the slider and its value */
}
.survey-question {
  display: flex;
  padding: 10px;
}
.btn-primary {
  background-color: rgb(6, 131, 118);
}
.btn-primary:hover,
.btn-primary:active {
  background-color: rgb(126, 8, 139);
}
</style>
