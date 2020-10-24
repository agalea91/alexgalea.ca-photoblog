<template>
  <div id="app">
    <div class="neighbour-album-nav">
      <!-- <p>{{postContent}}</p>
      <p>{{postContent.prev_url_path}}</p>
      <p>
          postContent.prev_year={{postContent.prev_year === ''}}<br>
          postContent.prev_month={{postContent.prev_month}}<br>
          postContent.prev_post_name={{postContent.prev_post_name}}<br>
      </p> -->

      <!-- <div :v-if="postContent.prev_post_name !== ''" :key="postContent.prev_post_name"><p>
        Inside prev test i-if<br>
        {{postContent.prev_post_name !== ''}}
      </p></div>
      <div :v-if="postContent.next_post_name !== ''" :key="postContent.next_post_name"><p>
        Inside next test i-if<br>
        {{postContent.next_post_name !== ''}}
      </p></div> -->
      <!-- <script type="application/ld+json" :v-html="test"></script> -->
      <!-- <script type="application/ld+json" :v-html="test(postContent)"></script> -->
      <!-- <div v-bind="test2">WHAT THE FUCK: {{test2}}</div> -->
      <div>
        <router-link
          :to="{ name: 'post', params: {
            year: postContent.prev_year,
            month: postContent.prev_month,
            post_name: postContent.prev_post_name
          }}"
        >
          ← {{postContent.prev_title}}
        </router-link> | <router-link
          :to="{ name: 'post', params: {
            year: postContent.next_year,
            month: postContent.next_month,
            post_name: postContent.next_post_name
          }}"
        >
         {{postContent.next_title}} →
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
            :id="'album-photo-'+index"
            class="album-photo-container"
            data-aos="fade"
            data-aos-duration="2000"
            data-aos-easing="ease-in-sine"
            data-aos-once="true"
        >
          <img
            :src="contentBlock.file"
            :alt="contentBlock.caption"
            class="full-width-photo"
          >
        <div class="caption-container">
          <div v-if="contentBlock.caption" class="caption-below-photo">{{contentBlock.caption}}</div>
        </div>
        </div>
      </div>

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
h1 {
  // font-family: 'Cinzel Decorative', cursive;
  font-size: 2rem;
  margin-bottom: 0;
}
.neighbour-album-nav {
    // padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #545454;
    }
  }
}
.album-photo-container {
  font-size: 15px;
}
.photo-reel-block {
  max-width: 100%;
}
.post-desc {
  font-family: 'Playfair Display', serif;
  padding-bottom: 50px;
  font-size: 1.2rem;
  display: inline-block;
  width: 600px;
  max-width: 90%;
}
.text-block {
  padding-top: 70px;
  padding-bottom: 70px;
  font-size: 1.2rem;
  display: inline-block;
  width: 500px;
  max-width: 90%;
  text-align: center;
}
.full-width-photo {
  width: 1440px;
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
