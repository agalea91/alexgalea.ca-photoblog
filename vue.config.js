// const IS_PRODUCTION = process.env.NODE_ENV === 'production'

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
  }
}
