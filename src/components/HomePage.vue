<template>
  <div class="hello">
    <div style="padding-bottom:100px;"></div>
    <h1>Alex Galea's Photoblog</h1>
    <p>
      Welcome to my photo gallery<br>
      I am glad that you've come.
    </p>
    <ul>
      <li v-for="item in resources" :key="item.posts">
        Post: {{ item.posts }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  props: {
    resources: Array
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
