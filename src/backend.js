import axios from 'axios'
// Set VUE_APP_API_ENDPOINT in .env.development and .env.production
// These are automatically loaded when the vue server starts
// https://cli.vuejs.org/guide/mode-and-env.html#environment-variables
axios.defaults.baseURL = process.env.VUE_APP_API_ENDPOINT

let $axios = axios.create({
  // baseURL: '/api/',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// // Request interceptor
// $axios.interceptors.request.use(function (config) {
//   config.headers['Authorization'] = 'My Token'
//   return config
// })

// Response interceptor
$axios.interceptors.response.use(function (response) {
  return response
}, function (error) {
  console.log(error)
  return Promise.reject(error)
})

export default {
  fetchPosts (args) {
    var _args = Object.assign({}, args)
    // console.log('Calling fetchPosts with args:')
    // console.log(_args)
    return $axios.get(`posts`, { params: _args })
      .then(response => {
        // console.log(response)
        return response.data
      })
  },
  fetchCategories (args) {
    var _args = Object.assign({}, args)
    // console.log('Calling fetchCategories with args:')
    // console.log(_args)
    return $axios.get(`categories`, { params: _args })
      .then(response => {
        // console.log(response)
        return response.data
      })
  }
}
