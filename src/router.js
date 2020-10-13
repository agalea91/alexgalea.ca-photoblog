import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import PhotoblogPost from './views/PhotoblogPost.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/filter/:year',
      name: 'home',
      component: Home
    },
    {
      path: '/album/:year/:month/:post_name',
      name: 'post',
      component: PhotoblogPost
    }
    // {
    //   path: '/about',
    //   name: 'about',
    //   component: About
    // }

  ]
})
