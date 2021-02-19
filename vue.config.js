// DO NOT EDIT LINE BELOW
// Prerender routes are dynamically added to this file
const prerenderRoutes = ['/', '/album/2020/08/1-The-Story-of-S7ayulh-Thunder', '/album/2020/10/1-Lakota-Dream-of-What-Was-to-Be', '/album/2020/11/1-The-Man-with-One-Hot-Side', '/album/2020/11/2-Totem-Pole-Coat-of-Arms', '/collections', '/about', '/cookies-policy', '/album/2020/04/1-Joy-in-Life', '/collection/Sunrise', '/collection/Pacific-Northwest', '/collection/Ocean', '/collection/Mythology', '/collection/Mountains', '/collection/Malazan', '/collection/Joy', '/collection/Hike', '/collection/God', '/collection/First-Nations', '/collection/Dog', '/collection/Death', '/collection/Cloudy', '/collection/Beach', '/collection/Totem-Pole', '/collection/Sunset']

const PrerenderSPAPlugin = require('prerender-spa-plugin')
const path = require('path')
const Renderer = PrerenderSPAPlugin.PuppeteerRenderer

// Does not work in vue.config.js - have to use CommonJS
// import prerenderRoutes from './website_prerender_routes.json'
// console.log(prerenderRoutes)

module.exports = {
  outputDir: 'dist',
  assetsDir: 'static',
  devServer: {
    proxy: {
      '/api*': {
        target: 'http://localhost:5000/'
        // Line below is for docker
        // target: 'http://server:5000/'
      }
    }
  },
  configureWebpack: {
    plugins: []
  }
}

if (process.env.NODE_ENV === 'production') {
  module.exports.configureWebpack.plugins = (module.exports.configureWebpack.plugins || []).concat([
    new PrerenderSPAPlugin({
    // Required - The path to the webpack-outputted app to prerender.
      staticDir: path.join(__dirname, 'dist'),
      // Required - Routes to render.
      routes: prerenderRoutes, // [ '/', '/about', '/album/2020/11/2-Totem-Pole-Coat-of-Arms' ],
      server: {
      // Normally a free port is autodetected, but feel free to set this if needed.
        port: 8080
      },
      renderer: new Renderer({

        // Optional - Display the browser window when rendering. Useful for debugging.
        headless: true

        // maxConcurrentRoutes: 1,

        //  Wait to render until the specified event is dispatched on the document.
        // eg, with `document.dispatchEvent(new Event('custom-render-trigger'))`
        // renderAfterDocumentEvent: 'page-rendered',
        // renderAfterTime: 15000,
        // renderAfterElementExists: '#app',
      })
    })
  ])
}
