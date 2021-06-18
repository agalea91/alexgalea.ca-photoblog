<template>

  <div id="app">
    <h1>About</h1>
    <div class="main-content">
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
        Download the high resolution JPG file for any photograph on the
        site. Watermark removed and full resolution (up to 4000px).
      </p>
      <ul>
        <li><a href="https://www.buymeacoffee.com/alexgalea/e/34863">PHOTO - Full Quality Digital Download ($20)</a></li>
        <li><a href="https://www.buymeacoffee.com/alexgalea/e/34864">ALBUM - Full Quality Digital Download ($50)</a></li>
      </ul>
      <p>
        10% of sales go to Indspire - a Canadian Indigenous registered
        charity that invests in the education of First Nations.
      </p>
      <p>
        CC BY-NC 3.0 for non-commercial use.
      </p>
      <h2>Commercial Licensing</h2>
      <p>
        Please contact alex@alexgalea.ca for commercial licensing. My
        per-image liscence costs are comparable to
        <a href="https://www.shutterstock.com/license-comparison">Shutterstock</a>.
      </p>
      <h2>Camera Specs</h2>
      <p>
        I've been shooting Canon SLRs since 2005. My lens setup:
      </p>
      <ul>
        <li>70-200mm f/4.0</li>
        <li>60mm f/2.8 macro</li>
        <li>17-50mm f/2.8</li>
      </ul>
    </div>
    <div id="buyme-coffee">
      <a href="https://www.buymeacoffee.com/alexgalea"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=☕&slug=alexgalea&button_colour=000000&font_colour=ffffff&font_family=Cookie&outline_colour=ffffff&coffee_colour=FFDD00"></a>
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
