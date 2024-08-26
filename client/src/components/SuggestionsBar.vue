<template>
  <div>
    <div :style="sidebarStyle" :class="['sidebar p-4', { 'sidebar--open': isSidebarOpen }]">
      <div class="tips-container">
        <div class="d-flex p-2 flex-column">
          <h5 class="p-2">Tips</h5>
          <ul class="list">
            <li>
              Share any details with Coach about careers you may be part of or interested in, so
              that Coach can provide advice relevant to your interests.
            </li>
            <li>
              Whenever you think the activity has reached a natural stopping point, you can tell
              Coach and it will help you finish the activity.
            </li>
          </ul>
        </div>
      </div>
      <div class="tips-container mt-3">
        <div class="d-flex p-2 flex-column">
          <h5 class="p-2">AI Prompt Suggestions</h5>
          <ul class="list">
            Here are some suggestions to improve your prompts to get better responses!
            <li v-for="(suggestion, index) in computedSuggestions" :key="index">
              {{ suggestion }}
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, Ref, computed } from 'vue'

export default defineComponent({
  name: 'SuggestionsBar',
  props: {
    suggestions: {
      type: Array as () => string[],
      default: () => []
    }
  },
  setup(props, { expose }) {
    const isSidebarOpen: Ref<boolean> = ref(true)
    const sidebarStyle: Ref<{ display?: string }> = ref({})

    const toggleSidebar = () => {
      isSidebarOpen.value = !isSidebarOpen.value
      if (isSidebarOpen.value) {
        setTimeout(() => {
          sidebarStyle.value = {
            display: 'flex'
          }
        }, 150) // Set your desired delay here (300ms in this example)
      } else {
        setTimeout(() => {
          sidebarStyle.value = {
            display: 'none' // Example dynamic style
          }
        }, 280)
      }
    }
    const computedSuggestions = computed(() => props.suggestions)

    expose({
      toggleSidebar,
      isSidebarOpen,
      computedSuggestions
    })

    return {
      isSidebarOpen,
      toggleSidebar,
      sidebarStyle,
      computedSuggestions
    }
  }
})
export interface SuggestionsBarInstance {
  toggleSidebar: () => void
  isSidebarOpen: Ref<boolean>
}
</script>

<style scoped>
.sidebar {
  max-width: 500px;
  height: 100%;
  border-left: 1px solid #ccc;
  background-color: rgb(244, 244, 249);
  color: white;
  display: flex;
  flex-direction: column;
  top: 0;
  left: 0;
  transform: translateX(100%);
  transition: transform 0.3s ease;
  overflow: hidden;
}
.sidebar--open {
  transform: translateX(0%);
}
.close-button {
  position: relative;
  top: -54%;
  left: 0%;
  z-index: 3;
}
.tips-container {
  background-color: white;
  border-radius: 5%;
  color: black;
  height: 50%;
  overflow: scroll;
  font-size: 14px;
}
.list {
}
.list li {
  padding: 10px;
  width: 100%;
  border-radius: 5px;
}
</style>
