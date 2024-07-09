import { createRouter, createWebHistory } from 'vue-router'
import AreYouCooked from '../components/AreYouCooked.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'AreYouCooked',
      component: AreYouCooked
    }
  ]
})

export default router
