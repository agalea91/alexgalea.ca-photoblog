<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      <a href="">Welcome</a> to my photoblog<br>
      I am glad that you've come.
    </p>
    <h3>Posts</h3>
    <ul>
      <li v-for="item in items" :key="item.message">
        {{ item.message }}
      </li>
      <li><a href="https://github.com/vuejs/awesome-vue" target="_blank">awesome-vue</a></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  props: {
    msg: String
  },
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
