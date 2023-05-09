<template>
  <Navbar />
  <BackgroundRemover/>
</template>

<script>

import Navbar from "./components/Navbar.vue";
import BackgroundRemover from "./components/BackgroundRemover.vue";

export default {
  name: 'App',
  components: {
    Navbar,
    BackgroundRemover
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  min-height: 100vh;
}
</style>
