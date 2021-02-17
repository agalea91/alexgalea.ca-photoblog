<template>

  <div id="app">
    <h1>Photo Collections</h1>
    <div id="h1-lower" class="header-homepage-link">Raven's Light | A Photo Journal</div>
    <div class="headline-below-h1">
      <p class="headline-main-text ">
        What are you curious about today?
      </p>
    </div>
    <div></div>
    <SearchBox defaultOpen />
  </div>
</template>

<script>
import SearchBox from '@/components/SearchBox.vue'
export default {
  name: 'CollectionList',
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
  font-size: 1.2rem;
  display: inline-block;
  width: 400px;
  max-width: 90%;
  height: 50px;
  margin-bottom: 0;
}
.headline-below-h1 {
  display: inline-block;
  padding: 20px;
  width: 280px;
  max-width: 90%;
}
</style>
