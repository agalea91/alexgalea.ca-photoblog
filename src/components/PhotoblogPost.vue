<template>
  <div class="hello">
    <div style="padding-bottom:100px;"></div>
    <h1>Alex Galea's Photoblog</h1>
    <p>
      Welcome to my photo gallery<br>
      I am glad that you've come.
    </p>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  props: {
    posts: Array
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
</style>
