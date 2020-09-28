<template>
  <div class="home">
    <HomePage
      testing="false"
      v-bind:posts="posts"
    />
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
      posts: [],
      error: ''
    }
  },
  methods: {
    fetchPosts () {
      $backend.fetchPosts()
        .then(responseData => {
          responseData.posts.forEach(post => {
            this.posts.push(post)
          })
        }).catch(error => {
          this.error = error.message
          console.log(error)
        })
    }
    // fetchSecureResource () {
    //   $backend.fetchSecureResource()
    //     .then(responseData => {
    //       this.resources.push(responseData)
    //     }).catch(error => {
    //       this.error = error.message
    //     })
    // }
  },
  mounted () {
    this.fetchPosts()
  }
}
</script>

<style lang="scss">

</style>
