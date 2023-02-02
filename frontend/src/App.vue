<!-- <script setup lang="ts"> -->
<!-- import HelloWorld from './components/HelloWorld.vue' -->
<!-- </script> -->

<template>
  <h1>Users <button @click="fetchUsers">🔄</button></h1>
  <p v-if="!users">Loading users...</p>
  <pre>{{ users }}</pre>
</template>

<script>
import { $fetch } from "ofetch";
import { ref, onMounted } from "vue";

export default {
  setup() {
    let users = ref(null);
    let logindata;
    const login = async () => {
      logindata = await $fetch("http://localhost:8000/login/", {
        method: "POST",
        body: {
          username: "admin",
          password: "admin",
        },
      });

      console.log(logindata);
    };
    const fetchUsers = async () => {
      users.value = null;
      users.value = await $fetch("http://localhost:8000/users/", {
        credentials: "include",
        headers: {
          Accept: "application/json",
        },
        // credentials: "same-origin",
      });
      console.log("prive");
    };
    onMounted(login);

    return { users, fetchUsers, logindata };
  },
};
</script>
