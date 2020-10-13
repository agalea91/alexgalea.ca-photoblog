<template>
  <div id="app">
    <div style="padding-bottom:100px;"></div>
    <h1>{{postContent.title}}</h1>
    <div class="desc-below-title">{{postContent.desc}}</div>
    <div v-for="(contentBlock, index) in postContent.body.divs" :key="index">
      <div v-if="contentBlock.type === 'text'">
        <div class="text-block">{{contentBlock.text}}</div>
      </div>
      <div v-if="contentBlock.type === 'photo'">
        <img
          :src="contentBlock.file"
          :alt="contentBlock.caption"
          class="full-width-photo"
        >
        <div class="caption-below-photo">{{contentBlock.caption}}</div>
      </div>
      <!-- <p>
        {{index}}
        {{contentBlock}}
      </p> -->
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
@import url("https://fonts.googleapis.com/css2?family=Cinzel+Decorative&family=Playfair+Display&display=swap");
html { width: 100%; }
#app {
  // font-family: 'Playfair Display', serif;
  font-size: 1.5rem;
}
h1 {
  // font-family: 'Cinzel Decorative', cursive;
  font-family: 'Playfair Display', serif;
  font-size: 4rem;
}
.desc-below-title {
  padding-bottom: 50px;
  font-size: 2rem;
}
.text-block {
  padding-bottom: 20px;
  font-size: 1.5rem;
}
.full-width-photo {
  padding-bottom: 20px;
  max-width: 100%;
}
.caption-below-photo {
  padding-bottom: 20px;
  font-size: 1rem;
}
</style>
