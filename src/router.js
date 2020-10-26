import Vue from 'vue'
import Router from 'vue-router'
import VueHead from 'vue-head'

import Home from './views/Home.vue'
import About from './views/About.vue'
import PhotoblogPost from './views/PhotoblogPost.vue'

Vue.use(VueHead)
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/collection/:year',
      name: 'collection',
      component: Home
    },
    {
      path: '/album/:year/:month/:post_name',
      name: 'post',
      component: PhotoblogPost
    },
    {
      path: '/about',
      name: 'about',
      component: About
    }

  ]
})
