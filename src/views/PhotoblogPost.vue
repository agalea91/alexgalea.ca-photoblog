<template>
  <div class="home">
    <PhotoblogPost
      testing="false"
      v-bind:postContent="postContent"
    />
  </div>
</template>

<script>
// @ is an alias to /src
import PhotoblogPost from '@/components/PhotoblogPost.vue'
import $backend from '../backend'
import AOS from 'aos'
import 'aos/dist/aos.css'

export default {
  name: 'home',
  components: {
    PhotoblogPost
  },
  data () {
    return {
      postContent: {
        'body': { 'divs': [] }
      },
      prevPostPath: '',
      nextPostPath: '',
      error: ''
    }
  },
  methods: {
    fetchPosts (args) {
      console.log('Fetching posts from vue frontend')
      $backend.fetchPosts(args)
        .then(responseData => {
          try {
            this.postContent = responseData.posts[0]
          } catch (err) {
            console.log(err)
          }
        }).catch(error => {
          this.error = error.message
          console.log(error)
        })
    }
  },
  created () {
    AOS.init()
  },
  mounted () {
    this.fetchPosts({
      year: this.$route.params.year,
      month: this.$route.params.month,
      foldername: this.$route.params.post_name,
      include_post_content: 'true'
    })
  }
}
</script>

<style lang="scss">
</style>
