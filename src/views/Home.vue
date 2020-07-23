<template>
  <div class="home">
    <HomePage testing="false"/>
    <!-- <HelloWorld msg="Welcome to Your Vue.js + Flask App"/> -->
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import HomePage from '@/components/HomePage.vue'

export default {
  name: 'home',
  components: {
    HelloWorld,
    HomePage
  }
}
</script>

<style lang="scss">

</style>
