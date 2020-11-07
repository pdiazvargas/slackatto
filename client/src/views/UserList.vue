<template>
  <div>
    <UserCard v-for="user in users" :key="user.id" :user="user"/>
  </div>
</template>

<script>
import UserCard from '@/components/UserCard.vue'
import SampleUsers from '@/sample/users'
import axios from 'axios'

export default {
  components: {
    UserCard
  },
  data() {
    return {
      users: []
    }
  },
  created() {
    axios
      .get('https://wkohg0bgy8.execute-api.us-east-2.amazonaws.com/Prod/users')  // Does a get request
      .then(response => {
        this.users = response.data;
      })
      .catch(error => {
        console.log('There was an error:', error.response) // Logs out the error
      })
  }
}
</script>

<style scoped>
</style>