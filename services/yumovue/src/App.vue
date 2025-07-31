<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <img alt="云曦墨染的杂货铺" class="logo" src="@/assets/logo.png" width="32" height="32" />
    <nav>
    <RouterLink to="/">Home</RouterLink>
    </nav>
  </header>

  <div>
    <RouterView />
  </div>

</template>

<style scoped>

header {
  display: flex;
  width: 100%;
  flex-direction: row;
  padding: 10px 1rem;
}

.logo {
  display: block;
  margin: 0 20px;
  float: left;
}


nav {
  overflow: hidden;
  display: block;
  align-content: baseline;
}

nav a {
  float: left;
  display: block;
  color: #bb3b3b;
  text-align: center;
  text-decoration: none;
}
</style>
