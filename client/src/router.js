import Vue from "vue";
import Router from "vue-router";
import Header from "./layout/starter/StarterHeader";
import Footer from "./layout/starter/StarterFooter";
import UserList from "./views/UserList.vue";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "user-list",
      components: {
        // header: Header,
        default: UserList,
        // footer: Footer
      }
    }
  ]
});
