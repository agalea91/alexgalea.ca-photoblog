const PrerenderSPAPlugin = require('prerender-spa-plugin')
const path = require('path')
const Renderer = PrerenderSPAPlugin.PuppeteerRenderer

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
      routes: [ '/', '/about', '/album/2020/11/2-Totem-Pole-Coat-of-Arms' ],
      server: {
      // Normally a free port is autodetected, but feel free to set this if needed.
        port: 8080
      },
      renderer: new Renderer({
        renderAfterTime: 15000,
        // renderAfterElementExists: '#app',
        // Optional - Display the browser window when rendering. Useful for debugging.
        headless: false
      //  Wait to render until the specified event is dispatched on the document.
      // eg, with `document.dispatchEvent(new Event('custom-render-trigger'))`
      // renderAfterDocumentEvent: 'page-rendered'
      })
    })
  ])
}
