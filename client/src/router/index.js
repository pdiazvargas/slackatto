import Vue from 'vue'
import VueRouter from 'vue-router'
import UserList from '../views/UserList.vue'
import UserDetails from '../views/UserDetails.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'user-list',
    component: UserList
  },
  {
    path: '/user/:id',
    name: 'user-show',
    component: UserDetails,
    props: true
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
