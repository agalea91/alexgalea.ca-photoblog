<template>
  <div class="home">
    <CollectionList />
  </div>
</template>

<script>
// @ is an alias to /src
import CollectionList from '@/components/CollectionList.vue'

export default {
  name: 'collections',
  components: {
    CollectionList
  },
  head: {
    title: {
      inner: 'Photo Collections'
    },
    meta: [
      {
        name: 'description',
        content: "Photo albums by topic - Landscapes from the Pacific Northwest and Canada's Rocky Mountains."
      }
    ]
  }
  // beforeRouteUpdate (to, from, next) {
  //   this.fetchPosts({
  //     include_post_content: 'false',
  //     year: next.$route.params.year
  //   })
  // }
}
</script>

<style lang="scss">
// .github-corner:hover .octo-arm{animation:octocat-wave 560ms ease-in-out}@keyframes octocat-wave{0%,100%{transform:rotate(0)}20%,60%{transform:rotate(-25deg)}40%,80%{transform:rotate(10deg)}}@media (max-width:500px){.github-corner:hover .octo-arm{animation:none}.github-corner .octo-arm{animation:octocat-wave 560ms ease-in-out}}
</style>
