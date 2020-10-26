<template>

  <div id="app">
    <h1>Alexander Galea's Photoblog</h1>
    <div class="headline-below-h1">
      <p>
        Welcome to my photo gallery<br>
        I am glad that you've come.
      </p>
    </div>
    <ul>
      <li v-for="post in posts" :key="post.url_path">
        <div class="post-summary">
          <div class="post-title">{{ post.title }}</div>
          <div class="post-desc">
            {{ post.desc }} (<i>{{ post.photos_taken_date }}</i>)
          </div>
          <router-link
            :to="{ name: 'post', params: {
              year: post.year,
              month: post.month,
              post_name: post.post_name
            }}"
          >
            <img
              :src="post.cover_image"
              alt="Cover image"
              class="post-cover-image"
            >
          </router-link>
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

.post-title {
  font-family: 'Playfair Display', serif;
  margin: 40px 0 0;
  text-align: left;
  padding-left: 10px;
  font-weight: bold;
  font-size: 1.7rem;
}
.post-desc {
  // font-family: 'Playfair Display', serif;
  margin: 10px 0 0;
  text-align: left;
  padding-left: 10px;
  font-weight:normal;
  font-size: 1rem;
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
  width: 1000px;
  max-width: 100%;
  margin-left:auto;
  margin-right:auto;
  line-height: 100%;
}
.post-cover-image {
  max-width: 100%;
  margin: 10px;
}
.headline-below-h1 {
  padding: 20px
}
</style>
