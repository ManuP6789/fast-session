<!-- AchievementModal.vue -->
<template>
  <div class="modal" tabindex="-1" role="dialog" style="display: block">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Congratulations!</h5>
        </div>
        <div
          class="modal-body d-flex flex-column align-items-center justify-content-center text-center"
        >
          <img :src="badgeImage" alt="Achievement Badge" class="badge-img" />
          <p>You have successfully completed the 15 Coach Activities!</p>
          <a href="https://www.linkedin.com/feed/" target="_blank" class="btn btn-primary">
            Share on LinkedIn
          </a>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" @click="$emit('close')">Close</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import badgeImage from '../assets/badgeLogoImage.png'

export default defineComponent({
  name: 'AchievementModal',

  data() {
    return {
      badgeImage
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
  z-index: 1052;
  overflow: hidden;
}
.badge-img {
  width: 250px;
  height: 250px;
}
.modal-dialog {
  margin: 10% auto;
}

.btn-primary {
  background-color: rgb(6, 131, 118);
}
.btn-primary:hover,
.btn-primary:active {
  background-color: rgb(126, 8, 139);
}
</style>
