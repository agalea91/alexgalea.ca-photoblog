<template>

  <div id="app">
    <h1>Raven's Light</h1>
    <div id="h1-lower" class="header-homepage-link">A Photo Journal</div>
    <div class="headline-below-h1">
      <p class="headline-main-text">
        In Native American legends, Raven is said to have brought light to the world.
        <br>
        <br>
        This gallery is a brief look into that world, through the lens of my camera.
        <br>
        <br>
        - Alex
      </p>
    </div>
    <div></div>
    <SearchBox/>
    <ul>
      <li v-for="post in posts" :key="post.url_path">
        <div class="post-summary">
          <router-link
            :to="{ name: 'post', params: {
              year: post.year,
              month: post.month,
              post_name: post.post_name
            }}"
          >
            <div class="post-title">{{ post.title }}</div>
          </router-link>
          <div class="post-desc">
            {{ post.photo.desc }} | <i>{{ post.photo.date_taken }}</i> | <i>{{ post.photo.location }}</i>
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
import SearchBox from '@/components/SearchBox.vue'
export default {
  name: 'HomePage',
  props: {
    posts: Array
  },
  components: {
    SearchBox
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

.headline-main-text {
  // font-family: 'Playfair Display', serif;
  font-family: 'Nothing You Could Do', cursive;
  padding-bottom: 25px;
  font-size: 1.2rem;
  display: inline-block;
  width: 400px;
  max-width: 90%;
  height: 50px;
}
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
  display: inline-block;
  padding: 20px;
  width: 280px;
  max-width: 90%;
}
</style>
