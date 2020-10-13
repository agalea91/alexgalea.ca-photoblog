<template>
  <div class="home">
    <!-- FORK Me -->
    <a href="https://github.com/agalea91/alexgalea.ca-photoblog"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://s3.amazonaws.com/github/ribbons/forkme_right_white_ffffff.png" alt="Fork me on GitHub"></a>
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
    fetchPosts (args) {
      console.log('Fetching posts from vue frontend')
      $backend.fetchPosts(args)
        .then(responseData => {
          try {
            responseData.posts.forEach(post => {
              this.posts.push(post)
            })
          } catch (err) {
            console.log(err)
          }
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
    this.fetchPosts({
      include_post_content: 'false',
      year: this.$route.params.year
    })
  },
  beforeRouteUpdate (to, from, next) {
    this.fetchPosts({
      include_post_content: 'false',
      year: next.$route.params.year
    })
  }
}
</script>

<style lang="scss">
</style>
