// const IS_PRODUCTION = process.env.NODE_ENV === 'production'

module.exports = {
  // publicPath: '/photoblog/',
  // By default, Vue CLI assumes your app will be deployed at the root of a domain, e.g. https://www.my-app.com/. If your app is deployed at a sub-path, you will need to specify that sub-path using this option. For example, if your app is deployed at https://www.foobar.com/my-app/, set publicPath to '/my-app/'.

  outputDir: 'dist',
  assetsDir: 'static',

  // baseUrl: IS_PRODUCTION
  // ? 'http://cdn123.com'
  // : '/',
  // For Production, replace set baseUrl to CDN
  // And set the CDN origin to `yourdomain.com/static`
  // Whitenoise will serve once to CDN which will then cache
  // and distribute
  devServer: {
    proxy: {
      '/api*': {
        // Forward frontend dev server request for /api to django dev server
        target: 'http://server:5000/'
      }
    }
  }
}
