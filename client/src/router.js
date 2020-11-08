import Vue from "vue";
import Router from "vue-router";
import UserList from "./views/UserList.vue";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "user-list",
      components: {
        default: UserList,
      }
    }
  ]
});
