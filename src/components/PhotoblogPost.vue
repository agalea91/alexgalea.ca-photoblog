<template>
  <div id="app">
    <div class="album-nav">
      <div :to="postContent.prev_url_path">
        <router-link :to="postContent.prev_url_path">
          ← {{postContent.prev_post}}
        </router-link>
      </div>
      <div :v-if="postContent.next_url_path">
        <router-link :to="postContent.next_url_path">
          {{postContent.next_post}} ->
        </router-link>
      </div>
    </div>
    <div style="padding-bottom:100px;"></div>
    <div class="post-desc">{{postContent.desc}}<br><i>{{postContent.photos_taken_date}}</i></div>
    <h1>{{postContent.title}}</h1>
    <div>{{this.$route.params.year}}-{{this.$route.params.month}}</div>
    <div class="photo-reel-block" v-for="(contentBlock, index) in postContent.body.divs" :key="index">
      <div v-if="contentBlock.type === 'text'">
        <div class="text-block">
          <p v-html="contentBlock.text"></p>
        </div>
      </div>
      <div v-if="contentBlock.type === 'photo'">
        <div
            :id="'album-photo-transition-'+index"
            data-aos="fade"
            data-aos-duration="2500"
            data-aos-easing="ease-in-sine"
        >
          <img
            :src="contentBlock.file"
            :alt="contentBlock.caption"
            class="full-width-photo"
          >
        </div>
        <div v-if="contentBlock.caption" class="caption-below-photo">{{contentBlock.caption}}</div>
      </div>

    </div>

  </div>
</template>

<script>

export default {
  name: 'PhotoblogPost',
  props: {
    postContent: Object
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
html { width: 100%; }
#app {
  // font-family: 'Playfair Display', serif;
  font-size: 1.5rem;
}
h1 {
  // font-family: 'Cinzel Decorative', cursive;
  font-size: 4rem;
  margin-bottom: 0;
}
.album-nav {
    padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #545454;
    }
  }
}
.photo-reel-block {
  max-width: 100%;
}
.post-desc {
  font-family: 'Playfair Display', serif;
  padding-bottom: 50px;
  font-size: 1.5rem;
  display: inline-block;
  width: 600px;
}
.text-block {
  padding: 70px;
  font-size: 1.7rem;
  display: inline-block;
  width: 500px;
  max-width: 90%;
  text-align: center;
}
.full-width-photo {
  width: 1440px;
  max-width: 100%;
}
.caption-below-photo {
  width: 1439px;
  max-width: 100%;
  padding-bottom: 20px;
  font-size: 1rem;
  display: inline-block;
  text-align: right;
}

// Horizontal line effect
h1 {
  display: flex;
  flex-direction: row;
}
h1:before, h1:after{
  content: "";
  flex: 1 1;
  border-bottom: 1px solid #000;
  margin: auto;
}
h1:before {
  margin-right: 10px
}
h1:after {
  margin-left: 10px
}
</style>
