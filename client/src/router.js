import Vue from "vue";
import Router from "vue-router";
import UserList from "./views/UserList.vue";
import NotFound from "./views/NotFound.vue";

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: "/",
      name: "user-list",
      components: {
        default: UserList,
      }
    },
    { path: '*', component: NotFound }
  ]
});
