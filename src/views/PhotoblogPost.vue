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
// import AOS from 'aos'

export default {
  name: 'home',
  components: {
    PhotoblogPost
  },
  data () {
    return {
      postContent: {
        'quote': {},
        'photo': {},
        'body': { 'divs': [] }
      },
      error: ''
    }
  },
  head: {
    title: function () {
      return {
        inner: this.postContent.title
      }
    },
    script: function () {
      return [{
        t: 'application/ld+json',
        i: this.postContent.jsonld_schema
      }]
    }
    // meta: function () {
    //   return [
    //     {
    //       name: 'description',
    //       content: this.postContent.photo.desc.replace(/\.$/, '') + '. High quality photos for download.'
    //     }
    //   ]
    // }
  },
  methods: {
    fetchPosts: function () {
      let args = {
        year: this.$route.params.year,
        month: this.$route.params.month,
        foldername: this.$route.params.post_name,
        include_post_content: 'true'
      }
      // console.log('Fetching posts from vue frontend')
      $backend.fetchPosts(args)
        .then(responseData => {
          try {
            this.postContent = responseData.posts[0]
            this.$emit('updateHead')
          } catch (err) {
            console.log(err)
          }
        }).catch(error => {
          this.error = error.message
          console.log(error)
        })
    }
    // imageObjectSchema: function (postContent) {
    //   let script = []
    //   for (const contentBlock in postContent.body.divs) {
    //     if (postContent.type === 'photo') {
    //       script.push({
    //         '@context': 'https://schema.org/',
    //         '@type': 'ImageObject',
    //         'contentUrl': 'https://' + location.host + contentBlock.file,
    //         'license': 'https://creativecommons.org/licenses/by-nc/4.0/',
    //         'acquireLicensePage': 'https://' + location.host + '/about'
    //       })
    //     }
    //   }
    //   return JSON.stringify(script)
    // },
    // test: function (postContent) {
    //   return 'console.log(\'im working\');'
    // }
  },
  // updated() {
  //   AOS.refreshHard()
  // },
  watch: {
    '$route': function (to, from) {
      this.fetchPosts()
    }
  },
  mounted () {
    this.fetchPosts()
  },
  serverPrefetch () {
    return this.fetchPosts()
  }
}
</script>

<style lang="scss">
</style>
