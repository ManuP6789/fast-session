import { createRouter, createWebHistory } from 'vue-router'
import Ping from '../components/Ping.vue'
import Books from '../components/Books.vue'
import Cooked from '../components/AreYouCooked.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Cooked',
      component: Cooked
    },
    {
      path: '/books',
      name: 'Books',
      component: Books
    },
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    }
  ]
})

export default router
