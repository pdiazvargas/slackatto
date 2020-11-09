<template>
    <div>
        <section class="section section-sm">
            <div class="container">
                <div class="row row-grid align-items-center">
                    <div class="col-md-6 order-md-1">
                        <div class="pr-md-5">
                            <h3>Workito Team Directory</h3>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <section class="section section-sm my-0 overflow-hidden">
            <div class="container py-0">
                <div class="row row-grid align-items-center">
                    <div class="col-lg-8">
                        <UserCard v-for="user in users" :key="user.id" :user="user"/>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
import axios from 'axios'
import UserCard from "@/components/UserCard";

export default {
  components: {
      UserCard
  },
  data: function() {
      return {
        users: []
      };
  },
  created() {
    axios
      .get('https://wkohg0bgy8.execute-api.us-east-2.amazonaws.com/Prod/users')
      .then(response => {
        this.users = response.data;
      })
      .catch(error => {
        console.log('There was an error:', error.response)
      })
  }
};
</script>
