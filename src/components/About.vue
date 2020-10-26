<template>

  <div id="app">
    <h1>About</h1>
    <div class="main-content">
      <p>
        I've been shooting Canon SLRs since 2005. My lens setup:
      </p>
      <ul>
        <li>70-200mm f/4.0</li>
        <li>60mm f/2.8 macro</li>
      </ul>
      <p>
        Living in Western Canada has given me the opportunity to photograph amazing scenery.
        <br><br>
        I've become fascinated by the stories of the native peoples of the Pacific North-West.
        They were here for thousands of years before we arrived, and oral histories have preserved their tales and legends.
        <br><br>
        My album narratives are also sourced from podcasts, books, or anything that I'm inspired by.
      </p>
      <h2>Licensing</h2>
      <p>
        Thanks for your interest! Please contact alex@alexgalea.ca for
        licensing inquiries. My per-image liscence costs are comparable to
        <a href="https://www.shutterstock.com/license-comparison">Shutterstock</a>.
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'About',
  props: {}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

.main-content {
  font-family: 'Playfair Display', serif;
  font-weight:normal;
  display: inline-block;
  width: 600px;
  max-width: 90%;

  margin: 5px 0 0;
  text-align: left;
  padding-left: 10px;
}
// ul {
//   list-style-type: none;
//   padding: 0;
// }
// li {
//   // display: inline-block;
//   margin: 30px;
// }
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
