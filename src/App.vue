<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link>
      | <router-link to="/filter/2020">2020</router-link>
      <!-- <router-link to="/about">About></router-link> -->
    </div>
    <router-view/>
  </div>
</template>

<style lang="scss">
// @import url('https://fonts.googleapis.com/css?family=Sree+Krushnadevaraya');
@import url("https://fonts.googleapis.com/css2?family=Cinzel+Decorative&family=Playfair+Display&family=Unna&display=swap");
// html { overflow-x: hidden }
#app {
  // font-family: Sree Krushnadevaraya,serif;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  // font-family: 'Playfair Display', serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;

  // Use the rem metric elsewhere, scale up or down with this value
  font-size: 20px;
}
body { margin: 0; }
h1 {
  font-family: 'Playfair Display', serif;
  // font-family: 'Avenir', Helvetica, Arial, sans-serif;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #545454;
    }
  }
}
#plus {
  padding: 0 20px 0 20px;
  display: inline-block;
  font-size: 3rem;
  vertical-align: top;
  line-height: 100px;
}

</style>
