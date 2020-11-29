<template>
  <div id="app">
    <router-link to="/" id="homepage-link" class="header-homepage-link">
      <div>Raven's Light</div>
      <div id="h1-lower">A Photo Journal</div>
    </router-link>
    <div class="neighbour-album-nav">
      <router-link
        v-if="postContent.next_post_name"
        :to="{ name: 'post', params: {
          year: postContent.next_year,
          month: postContent.next_month,
          post_name: postContent.next_post_name
        }}"
        style="padding-left: 25px;"
      >
        {{postContent.next_title}} →
      </router-link>
      <br>
      <router-link
        v-if="postContent.prev_post_name"
        :to="{ name: 'post', params: {
          year: postContent.prev_year,
          month: postContent.prev_month,
          post_name: postContent.prev_post_name
        }}"
        style="padding-right: 25px;"
      >
        ← {{postContent.prev_title}}
      </router-link>
    </div>
    <div style="padding-bottom:25px;"></div>
    <h1>{{postContent.title}}</h1>
    <div class="post-author">
      {{ postContent.photo.date_taken }} | {{ postContent.photo.location }}
      <!-- {{this.$route.params.year}}-{{this.$route.params.month}} -->
    </div>
    <div class="post-desc">
      {{postContent.photo.desc}}
      <!-- {{postContent.photo.desc}} | {{postContent.photo.date_taken}} | {{postContent.photo.location}} -->
    </div>
    <div class="photo-reel">
      <div class="photo-reel-block" v-for="(contentBlock, index) in postContent.body.divs" :key="index">
        <div v-if="contentBlock.type === 'text'">
          <div class="text-block">
            <p v-html="contentBlock.text"></p>
          </div>
        </div>
        <div v-if="contentBlock.type === 'photo'">
          <div
              class="album-photo-container"
              data-aos="fade"
              data-aos-duration="2000"
              data-aos-easing="ease-in-sine"
              data-aos-once="true"
          >
            <img
              :src="contentBlock.file"
              :alt="contentBlock.caption"
              :id="'album-photo-'+index"
              class="full-width-photo"
            >
          <div class="caption-container">
            <div v-if="contentBlock.caption" class="caption-below-photo">{{contentBlock.caption}}</div>
          </div>
          </div>
        </div>
      </div>
    </div>
    <div class="text-block" id="author-text" v-if=postContent.quote.attribution>
      - <i>{{postContent.quote.attribution}}</i>
    </div>

  </div>
</template>

<script>

export default {
  name: 'PhotoblogPost',
  props: {
    postContent: Object,
    error: String
  }
  // methods: {
  //   test: Function
  // }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
html { width: 100%; }
// #app {
  // font-family: 'Playfair Display', serif;

  // Use the rem metric elsewhere, scale up or down with this value
  // font-size: 1.5rem;
  // font-size: 1vw;
// }

#h1-lower {
  font-size: 40%;
}
h1 {
  // font-family: 'Cinzel Decorative', cursive;
  font-size: 2rem;
  margin-bottom: 0;
}
.neighbour-album-nav {
    // padding: 30px;
  font-family: 'Playfair Display', serif;
  line-height: 25px;
  font-size: 1rem;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #545454;
    }
  }
}
.album-photo-container {
  width: 1080px;
  max-width: 100%;
  display: inline-block;
}
.photo-reel-block {
  max-width: 100%;
}
.post-author {
  font-size: 0.7rem;
  padding-bottom: 50px;
}
.post-desc {
  // font-family: 'Playfair Display', serif;
  font-family: 'Nothing You Could Do', cursive;
  padding-bottom: 25px;
  font-size: 2rem;
  display: inline-block;
  width: 400px;
  max-width: 90%;
  height: 50px;
}
.text-block {
  font-family: 'Playfair Display', serif;
  padding-top: 70px;
  padding-bottom: 70px;
  font-size: 1.3rem;
  display: inline-block;
  width: 500px;
  max-width: 90%;
  text-align: center;
}
#author-text {
  margin-top: 0;
  padding-top: 0;
}
.full-width-photo {
  max-width: 100%;
  font-size: 0px;
}
.caption-container {
  box-sizing: border-box;
  padding: 10px;
}
.caption-below-photo {
  width: 1439px;
  max-width: 100%;
  padding-bottom: 20px;
  padding-left: 10px;
  font-size: 1rem;
  display: inline-block;
  text-align: left;
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
