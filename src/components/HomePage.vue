<template>
  <div class="hello">
    <div style="padding-bottom:100px;"></div>
    <h1>Alex Galea's Photoblog</h1>
    <p>
      Welcome to my photo gallery<br>
      I am glad that you've come.
    </p>
    <ul>
      <li v-for="post in posts" :key="post.title">
        <div class="post-summary">
          <h3>
            <b>{{ post.title }}</b>. <i>{{ post.date }}</i>
          </h3>
          <a :href="post.url_path">
            <img
              :src="post.cover_image"
              alt="Cover image"
              class="post-cover-image"
            >
          </a>
        </div>
      </li>
    </ul>
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
h3 {
  font-weight:normal;
  margin: 40px 0 0;
  text-align: left;
  padding-left: 10px;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  // display: inline-block;
  margin: 30px;
}
a {
  color: #42b983;
}
.post-summary {
  width: 300px;
  max-width: 80%;
  margin-left:auto;
  margin-right:auto;
}
.post-cover-image {
  max-width: 100%;
  margin: 10px;
}
</style>
