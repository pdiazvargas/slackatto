<template>
    <card class="mt-1">
        <div class="d-flex">
            <div>
                <img
                    class="rounded-circle img-center img-fluid img-outline"
                    :data-src="user.profile.image_192"
                    :src="user.profile.image_192"
                    lazy="loaded"
                    style="width: 100px">
            </div>
            <div class="pl-4">
                <h5 class="title text-success">{{user.real_name}}</h5>
                <small class="title text-success">{{user.status || "No status available"}}</small>
                <div>
                    <label>username</label>
                    <span class="h6 text-muted pl-2">{{user.profile.display_name || "N/a"}}</span>
                </div>
                <div>
                    <label>title</label>
                    <span class="h6 text-muted pl-2">{{user.profile.title || "N/a"}}</span>
                </div>
                <div>
                    <label>phone</label>
                    <span class="h6 text-muted pl-2">{{user.profile.phone || "N/a"}}</span>
                </div>
                <div>
                    <badge v-if="user.is_admin" type="primary" rounded>admin</badge>
                    <badge v-if="user.is_owner" type="primary" rounded>owner</badge>
                    <badge v-if="!user.is_bot" type="primary" rounded>not a bot</badge>
                </div>
            </div>
        </div>
    </card>
</template>

<script>
export default {
  props: {
    user: {
      type: Object,
    }
  }
}
</script>

<style>

</style>