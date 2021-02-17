<template>
  <div id="app">
    <GdprAlert/>
    <div id="nav">
      <div v-if="this.$route.name === 'home'">
        <router-link to="/">Home</router-link>
        | <router-link to="/about">About</router-link>
        | <router-link to="/collections">Collections</router-link>
      </div>
      <div v-if="this.$route.name === 'collection'">
        <router-link to="/">Home</router-link>
        | <router-link to="/about">About</router-link>
        | <router-link to="/collections">Collections</router-link>
      </div>
      <div v-if="this.$route.name === 'collections'">
        <router-link to="/">Home</router-link>
        | <router-link to="/about">About</router-link>
      </div>
      <div v-if="this.$route.name === 'about'">
        <router-link to="/">Home</router-link>
      </div>
      <div v-if="this.$route.name === 'cookies-policy'">
        <router-link to="/">Home</router-link>
      </div>
      <div v-if="this.$route.name === 'post'">
      </div>
    </div>
    <router-view/>
    <div id="footer">
      <router-link to="/">Home</router-link>
      | <router-link to="/about">About</router-link>
      <br>
      <br>
      © Alexander Galea {{ new Date().getFullYear() }}
    </div>
  </div>
</template>

<script>
import GdprAlert from '@/components/GdprAlert.vue'
export default {
  name: 'App',
  components: {
    GdprAlert
  }
}
</script>

<style lang="scss">
// @import url('https://fonts.googleapis.com/css?family=Sree+Krushnadevaraya');
@import url("https://fonts.googleapis.com/css2?family=Cinzel+Decorative&family=Playfair+Display&family=Unna&family=Nothing+You+Could+Do&display=swap");
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
  // font-size: 20px;
  font-size: 20px;
  @media only screen and (max-width: 768px) {
    font-size: 15;
  }

  @media only screen and (max-width: 320px) {
    font-size: 10px;
  }

}
body { margin: 0; }

a {
  font-weight: bold;
  color: #2c3e50;
  &.router-link-exact-active {
    color: #545454;
  }
}

// H1 - internal homepage linking header
h1 {
  font-family: 'Playfair Display', serif;
  // font-family: 'Avenir', Helvetica, Arial, sans-serif;
  margin-bottom: 0;
  padding-bottom: 0;
}
#h1-lower{
  margin-top: 0;
  padding-top: 0;
  font-size: 1rem;
}
.header-homepage-link{
  font-family: 'Playfair Display', serif;
  text-decoration: none;
  color: #2c3e50;
  display: block;
  font-size: 2em;
  margin-top: 0.67em;
  margin-bottom: 0.67em;
  margin-left: 0;
  margin-right: 0;
  font-weight: bold;
}

// Nav - navigation elements
#nav {
  padding: 30px;
}
#footer {
  font-size: 1rem;
  padding-top: 100px;
  padding-bottom: 30px;
}
#plus {
  padding: 0 20px 0 20px;
  display: inline-block;
  font-size: 3rem;
  vertical-align: top;
  line-height: 100px;
}

// GDPR banner
#gdpr-alert {
  font-size: 12px;
}

</style>
