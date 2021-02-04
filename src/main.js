import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import './filters'

// import AOS from 'aos'
// import 'aos/dist/aos.css'

Vue.config.productionTip = false

new Vue({
  // el: '#app',
  // created () {
  //   AOS.init({
  //     disable: 'mobile'
  //   })
  // },
  router,
  store,
  render: h => h(App),
  mounted () {
    // You'll need this for renderAfterDocumentEvent.
    // document.dispatchEvent(new Event('page-rendered'))
  }
}).$mount('#app')
