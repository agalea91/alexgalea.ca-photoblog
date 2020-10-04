<template>
  <div class="home">
    <PhotoblogPost
      testing="false"
      v-bind:post="post"
    />
  </div>
</template>

<script>
// @ is an alias to /src
import PhotoblogPost from '@/components/PhotoblogPost.vue'
import $backend from '../backend'

export default {
  name: 'home',
  components: {
    PhotoblogPost
  },
  data () {
    return {
      post: {},
      error: ''
    }
  },
  methods: {
    fetchPostData () {
      $backend.fetchPostData()
        .then(responseData => {
          this.posts = responseData
        }).catch(error => {
          this.error = error.message
          console.log(error)
        })
    },
    mounted () {
      this.fetchPostData()
    }
  }
}
</script>

<style lang="scss">

</style>
