<template>
    <div class="event-card -shadow">
      <h4 class="title">{{ user.name }}</h4>
    </div>
</template>

<script>
export default {
  props: {
    user: {required: true, type: Object}
  }
}
</script>

<style scoped>
  .event-card {
    padding: 20px;
    margin-bottom: 24px;
    transition: all 0.2s linear;
    cursor: pointer;
  }
  .event-card:hover {
    transform: scale(1.01);
    box-shadow: 0 1px 5px 0 rgba(0, 0, 0, 0.2), 0 1px 5px 0 rgba(0, 0, 0, 0.19);
  }
  .event-card > .title {
    margin: 0;
  }

  .event-link {
    color: black;
    text-decoration: none;
    font-weight: 100;
  }
</style>
