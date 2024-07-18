<template>
  <div class="header d-flex flex-column justify-content-between">
    <div class="d-flex flex-column p-4 h-100">
      <div class="d-flex align-items-center flex-row">
        <img :src="logoSrc" alt="Logo" class="logo mr-3" style="height: 65px" />
      </div>
      <div class="d-flex flex-column justify-content-between h-100">
        <nav class="mt-3">
          <ul class="list">
            <li class="list-inline-item">
              <router-link to="/Home" class="text-decoration-none px-2 py-1 my-2" exact>
                <img
                  :src="home"
                  :class="{ 'nav-icon': true, 'active-icon': $route.path === '/Home' }"
                />
                Home
              </router-link>
            </li>
            <li class="list-inline-item">
              <router-link to="/" class="text-decoration-none px-2 py-1 my-2" exact>
                <img
                  :src="addBox"
                  :class="{ 'nav-icon': true, 'active-icon': $route.path === '/' }"
                />
                Find Activities
              </router-link>
            </li>
            <li class="list-inline-item">
              <router-link to="/History" class="text-decoration-none px-2 py-1 my-2" exact>
                <img
                  :src="history"
                  :class="{ 'nav-icon': true, 'active-icon': $route.path === '/History' }"
                />
                History
              </router-link>
            </li>
          </ul>
        </nav>
        <nav class="mt-3">
          <ul class="list">
            <li class="list-inline-item">
              <router-link to="/Feedback" class="text-decoration-none px-2 py-1 my-2" exact>
                <img
                  :src="feedback"
                  :class="{ 'nav-icon': true, 'active-icon': $route.path === '/Feedback' }"
                />
                Feedback
              </router-link>
            </li>
            <li class="list-inline-item">
              <router-link to="/Help" class="text-decoration-none px-2 py-1 my-2" exact>
                <img
                  :src="help"
                  :class="{ 'nav-icon': true, 'active-icon': $route.path === '/Help' }"
                />
                Help
              </router-link>
            </li>
            <li class="list-inline-item">
              <router-link to="/About" class="text-decoration-none px-2 py-1 my-2" exact>
                <img
                  :src="about"
                  :class="{ 'nav-icon': true, 'active-icon': $route.path === '/About' }"
                />
                About
              </router-link>
            </li>
          </ul>
        </nav>
      </div>
    </div>
    <div class="name px-4 py-2">
      <div class="logo-circle user-circle d-flex">
        <span class="user-icon">{{ firstLetter }}</span>
      </div>
      <h6 class="p-2">{{ name }}</h6>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType, computed } from 'vue'
import addBox from '../assets/icons/add_box_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.png'
import history from '../assets/icons/history_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.png'
import home from '../assets/icons/home_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.png'
import feedback from '../assets/icons/add_comment_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.png'
import about from '../assets/icons/info_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.png'
import help from '../assets/icons/help_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.png'

export default defineComponent({
  name: 'HeaderSection',
  props: {
    logoSrc: {
      type: String as PropType<string>,
      required: true
    },
    name: {
      type: String as PropType<string>,
      required: true
    }
  },
  setup(props) {
    const firstLetter = computed(() => props.name.charAt(0).toUpperCase())

    return {
      firstLetter
    }
  },
  data() {
    return {
      addBox,
      history,
      home,
      feedback,
      about,
      help
    }
  }
})
</script>

<style scoped>
.header {
  background-color: rgb(244, 244, 249);
  border-right: 1px solid #ccc;
  height: 100%;
  width: 25%;
}
.logo-circle {
  height: 28px;
  width: 28px;
  border-radius: 50%;
}
.user-circle {
  background-color: rgb(6, 131, 118);
}
.user-icon {
  margin: auto;
  height: 18px;
  width: 14px;
  font-size: 14px;
  align-items: center;
  text-align: center;
  color: white;
}
.name {
  border-top: 1px solid #ccc;
  display: flex;
  align-items: center;
}
.list {
  padding: 0;
  margin: 0;
  list-style: none;
}
.list li {
  display: block;
  width: 100%;
  border-radius: 5px;
}
.text-decoration-none {
  padding-left: 5px;
  border-radius: 5px;
  display: block;
  width: 100%;
  text-decoration: none;
  color: inherit;
}
.text-decoration-none:hover {
  background-color: #d5d3d3b8;
}
.text-decoration-none.router-link-active {
  background-color: rgb(6, 131, 118);
  color: white;
}
.nav-icon {
  height: 24px;
  width: 24px;
  margin-right: 8px;
  margin-bottom: 4px;
  filter: grayscale(100%) brightness(30%);
}
.active-icon {
  filter: grayscale(0%); /* White color */
}
</style>
