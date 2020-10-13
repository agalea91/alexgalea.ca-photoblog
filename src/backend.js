import axios from 'axios'

let $axios = axios.create({
  baseURL: '/api/',
  timeout: 5000,
  headers: { 'Content-Type': 'application/json' }
})

// Request Interceptor
$axios.interceptors.request.use(function (config) {
  config.headers['Authorization'] = 'Fake Token'
  return config
})

// Response Interceptor to handle and log errors
$axios.interceptors.response.use(function (response) {
  return response
}, function (error) {
  // Handle Error
  console.log(error)
  return Promise.reject(error)
})

export default {

  fetchPosts (args) {
    var _args = Object.assign({}, args)
    console.log('Calling fetchPosts with args:')
    console.log(_args)
    return $axios.get(`posts`, { params: _args })
      .then(response => {
        console.log(response)
        return response.data
      })
  }
  // fetchSecureResource () {
  //   return $axios.get(`secure-resource/zzz`)
  //     .then(response => response.data)
  // }
}
