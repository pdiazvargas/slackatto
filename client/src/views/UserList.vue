<template>
  <div>
    <UserCard v-for="user in users" :key="user.id" :user="user"/>
  </div>
</template>

<script>
import UserCard from '@/components/UserCard.vue'
import SampleUsers from '@/sample/users'
// import axios from 'axios'

export default {
  components: {
    UserCard
  },
  data() {
    return {
      users: SampleUsers.users
    }
  },
  // created() {
  //   axios
  //     .get('http://localhost:3000/events')  // Does a get request
  //     .then(response => {
  //       console.log(response.data) // For now, logs out the response
  //     })
  //     .catch(error => {
  //       console.log('There was an error:', error.response) // Logs out the error
  //     })
  // }
}
</script>

<style scoped>
</style>