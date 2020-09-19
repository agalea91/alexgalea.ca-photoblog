<template>
  <div class="home">
    <HomePage testing="false" v-bind:resources="resources"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HomePage from '@/components/HomePage.vue'
import $backend from '../backend'

export default {
  name: 'home',
  components: {
    HomePage
  },
  data () {
    return {
      resources: [],
      error: ''
    }
  },
  methods: {
    fetchPosts () {
      $backend.fetchPosts()
        .then(responseData => {
          this.resources.push(responseData)
        }).catch(error => {
          this.error = error.message
        })
    },
    fetchSecureResource () {
      $backend.fetchSecureResource()
        .then(responseData => {
          this.resources.push(responseData)
        }).catch(error => {
          this.error = error.message
        })
    }
  }
}
</script>

<style lang="scss">

</style>
