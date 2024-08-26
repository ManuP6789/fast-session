<template>
  <div class="modal-backdrop" @click="closeModal">
    <div class="modal" tabindex="-1" @click.stop>
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Activity Information</h5>
          </div>
          <div class="modal-body">
            <div><h6>Networking: The basics</h6></div>
            <form @submit.prevent="submitUserInfo">
              <div class="mb-3">
                <label for="name" class="form-label">What is your name?</label>
                <input
                  type="text"
                  class="form-control"
                  id="name"
                  v-model="userInfo.name"
                  required
                />
              </div>
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
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

export default defineComponent({
  name: 'UserModal',
  emits: ['submit'],
  setup(_, { emit }) {
    const userInfo = ref({
      goal: '',
      field: '',
      stage: '',
      name: ''
    })

    const submitUserInfo = () => {
      emit('submit', userInfo.value)
    }

    const closeModal = () => {
      emit('close')
    }

    return {
      userInfo,
      submitUserInfo,
      closeModal
    }
  }
})
</script>

<style scoped>
.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  z-index: 1040;
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
.modal-dialog {
  position: relative;
}
.modal-content {
  padding: 20px;
}
.btn {
  background-color: rgb(6, 131, 118);
}
.btn-primary:hover {
  background-color: rgb(126, 8, 139);
}
</style>
