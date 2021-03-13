<template>
  <div class="row column header" id="search-box-container">
    <div class="medium-6 medium-offset-3 ctrl">
      <form class="searchForm" v-on:submit.prevent="">
      <!-- <form class="searchForm" v-on:submit.prevent="delaySubmitSearch"> -->
        <input type="text" v-model="searchQuery" placeholder="sunset, clouds, mythology, ..." @keyup="delaySubmitSearch">
        <span class="removeInput" @click="removeSearchQuery">+</span>
      </form>
    </div>
    <div class="searchResult" v-show="isResult">
      <transition-group name="expand" tag="div">
        <router-link
          :to="{ name: 'collection', params: {
            tag: category.name.replace(' ', '-')
          }}"
          v-for="category in catResults"
          v-bind:key="category.key"
        >
          <div class="medium-8 medium-offset-2 columns card">
            <h2 class="text-headline">{{ category.name }}</h2>
            <p class="text-body-1">{{ category.desc }}</p>
          </div>
        </router-link>
      </transition-group>
    </div>
  </div>
</template>

<script>
import $backend from '../backend'
export default {
  name: 'SearchBox',
  props: {
    defaultOpen: Boolean
  },
  data () {
    return {
      catResults: null,
      isResult: false,
      searchQuery: '',
      searchTimeoutId: ''
    }
  },
  methods: {
    removeSearchQuery () {
      this.searchQuery = ''
      this.isResult = false
    },
    delaySubmitSearch () {
      let delay = 1000
      clearTimeout(this.searchTimeoutId)
      this.searchTimeoutId = setTimeout(() => {
        // Identical to submitSearch function
        this.catResults = []
        $backend.fetchCategories({
          search_phrase: this.searchQuery
        })
          .then(responseData => {
            try {
              responseData.categories.forEach(cat => {
                this.catResults.push(cat)
              })
              this.isResult = true
            } catch (err) {
              console.log(err)
            }
          }).catch(error => {
            this.error = error.message
            console.log(error)
          })
      }, delay)
    },
    submitSearch () {
      // Identical to delaySubmitSearch setTimout function
      this.catResults = []
      $backend.fetchCategories({
        search_phrase: this.searchQuery
      })
        .then(responseData => {
          try {
            responseData.categories.forEach(cat => {
              this.catResults.push(cat)
            })
            this.isResult = true
          } catch (err) {
            console.log(err)
          }
        }).catch(error => {
          this.error = error.message
          console.log(error)
        })
    }
  },
  watch: {
    '$route': function (to, from) {
      this.removeSearchQuery()
      if (this.$props.defaultOpen) {
        this.searchQuery = ''
        this.submitSearch()
      }
    }
  },
  mounted () {
    if (this.$props.defaultOpen) {
      this.searchQuery = ''
      this.submitSearch()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
#search-box-container {
  width: 90%;
  display: inline-block;
}
a {
  text-decoration: none;
}
.card {
  text-align: left;
  border-radius: 0;
  background: #fff;
  box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.13), 0 1px 5px 0 rgba(0, 0, 0, 0.08);
  padding: 1rem;
  transition: .4s ease-out
}
.card:hover {
  background-color: lightgray;
  color: black;
  box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.13), 0 3px 5px 0 rgba(0, 0, 0, 0.08);
}
.ctrl {
  margin-bottom: 1.6rem;
}
.header {
  color: #555;
  height: 100%;
  text-align: center;
  padding-top: 5px;
}
.header .cover-heading {
  font-size: 46px;
  color: #000;
  margin-top: 1.6rem;
  margin-bottom: 1.6rem;
}
.removeInput {
  font-size: 36px;
  color: #ddd;
  cursor: pointer;
  top: 0;
  right: 0;
  position: absolute;
  -webkit-transform: rotate(45deg);
  transform: rotate(45deg);
}
.searchForm {
  margin-bottom: 2.6rem;
  position: relative;
}
.text-headline {
  font-size: 20px;
  font-weight: bold;
  margin: 0;
  padding-top: 0;
  padding-bottom: 5px;
  letter-spacing: 0;
}
.text-body-1 {
  font-size: 15px;
  font-weight: normal;
  margin: 0;
  padding-top: 0;
  padding-bottom: 0;
  letter-spacing: 0;
}
/* vuejs transition */
.expand-transition {
  transition: all .5s ease;
  padding: 10px;
  min-height: 1500px;
  overflow: hidden;
  transition-delay: .5s;
}
.expand-enter, .expand-leave {
  height: 0;
  padding: 0 10px;
  opacity: 0;
}
/* Material Design code below */
.raised-button {
    display: inline-block;
    text-align: center;
    line-height: 1;
    cursor: pointer;
    -webkit-appearance: none;
    transition: all 0.25s ease-out;
    vertical-align: middle;
    border: 1px solid transparent;
    border-radius: 2px;
    padding: 0.85em 1em;
    margin: 0 1rem 1rem 0;
    font-size: 0.9rem;
    background: green;
    color: #FAFAFA;
}
.raised-button:hover, .raised-button:focus {
    background: green;
    color: #FFF;
    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.13), 0 1px 5px 0 rgba(0, 0, 0, 0.08);
}
input:focus { outline:none; }
[type="text"], [type="password"], [type="date"], [type="datetime"], [type="datetime-local"], [type="month"], [type="week"], [type="email"], [type="number"], [type="search"], [type="tel"], [type="time"], [type="url"], [type="color"], textarea {
    display: block;
    box-sizing: border-box;
    width: 100%;
    height: 2.4375rem;
    padding: 0.5rem;
    border: 0;
    margin: 0 0 1rem;
    font-family: inherit;
    font-size: 1rem;
    color: #9e9e9e;
    background-color: white;
    box-shadow: none;
    border-radius: 0;
    transition: box-shadow 0.5s, border-color 0.25s ease-in-out;
    -webkit-appearance: none;
    -moz-appearance: none;
}
input[type="text"], input[type="password"], input[type="date"], input[type="datetime"], input[type="datetime-local"], input[type="month"], input[type="week"], input[type="email"], input[type="number"], input[type="search"], input[type="tel"], input[type="time"], input[type="url"], input[type="color"], textarea {
  padding: 1rem 0 0.5rem 0;
  margin: 1.75rem 0 0.5rem;
  border-bottom: 1px solid #e0e0e0;
  border-radius: 0;
  background: transparent;
}
input[type="text"]::-webkit-input-placeholder, input[type="text"]::-webkit-input-placeholder, input[type="password"]::-webkit-input-placeholder, input[type="password"]::-webkit-input-placeholder, input[type="date"]::-webkit-input-placeholder, input[type="date"]::-webkit-input-placeholder, input[type="datetime"]::-webkit-input-placeholder, input[type="datetime"]::-webkit-input-placeholder, input[type="datetime-local"]::-webkit-input-placeholder, input[type="datetime-local"]::-webkit-input-placeholder, input[type="month"]::-webkit-input-placeholder, input[type="month"]::-webkit-input-placeholder, input[type="week"]::-webkit-input-placeholder, input[type="week"]::-webkit-input-placeholder, input[type="email"]::-webkit-input-placeholder, input[type="email"]::-webkit-input-placeholder, input[type="number"]::-webkit-input-placeholder, input[type="number"]::-webkit-input-placeholder, input[type="search"]::-webkit-input-placeholder, input[type="search"]::-webkit-input-placeholder, input[type="tel"]::-webkit-input-placeholder, input[type="tel"]::-webkit-input-placeholder, input[type="time"]::-webkit-input-placeholder, input[type="time"]::-webkit-input-placeholder, input[type="url"]::-webkit-input-placeholder, input[type="url"]::-webkit-input-placeholder, input[type="color"]::-webkit-input-placeholder, input[type="color"]::-webkit-input-placeholder, textarea::-webkit-input-placeholder, textarea::-webkit-input-placeholder {
  color: rgba(0, 0, 0, 0.26);
}
input[type="text"]:-moz-placeholder, input[type="text"]::-moz-placeholder, input[type="password"]:-moz-placeholder, input[type="password"]::-moz-placeholder, input[type="date"]:-moz-placeholder, input[type="date"]::-moz-placeholder, input[type="datetime"]:-moz-placeholder, input[type="datetime"]::-moz-placeholder, input[type="datetime-local"]:-moz-placeholder, input[type="datetime-local"]::-moz-placeholder, input[type="month"]:-moz-placeholder, input[type="month"]::-moz-placeholder, input[type="week"]:-moz-placeholder, input[type="week"]::-moz-placeholder, input[type="email"]:-moz-placeholder, input[type="email"]::-moz-placeholder, input[type="number"]:-moz-placeholder, input[type="number"]::-moz-placeholder, input[type="search"]:-moz-placeholder, input[type="search"]::-moz-placeholder, input[type="tel"]:-moz-placeholder, input[type="tel"]::-moz-placeholder, input[type="time"]:-moz-placeholder, input[type="time"]::-moz-placeholder, input[type="url"]:-moz-placeholder, input[type="url"]::-moz-placeholder, input[type="color"]:-moz-placeholder, input[type="color"]::-moz-placeholder, textarea:-moz-placeholder, textarea::-moz-placeholder {
  color: rgba(0, 0, 0, 0.26);
}
input[type="text"]:focus, input[type="password"]:focus, input[type="date"]:focus, input[type="datetime"]:focus, input[type="datetime-local"]:focus, input[type="month"]:focus, input[type="week"]:focus, input[type="email"]:focus, input[type="number"]:focus, input[type="search"]:focus, input[type="tel"]:focus, input[type="time"]:focus, input[type="url"]:focus, input[type="color"]:focus, textarea:focus {
  border: none;
  border-bottom: 2px solid #000;
  box-shadow: none;
  position: relative;
  top: 1px;
  background: transparent;
}
input[type="text"].with-floating-label + label.floating-label, input[type="password"].with-floating-label + label.floating-label, input[type="date"].with-floating-label + label.floating-label, input[type="datetime"].with-floating-label + label.floating-label, input[type="datetime-local"].with-floating-label + label.floating-label, input[type="month"].with-floating-label + label.floating-label, input[type="week"].with-floating-label + label.floating-label, input[type="email"].with-floating-label + label.floating-label, input[type="number"].with-floating-label + label.floating-label, input[type="search"].with-floating-label + label.floating-label, input[type="tel"].with-floating-label + label.floating-label, input[type="time"].with-floating-label + label.floating-label, input[type="url"].with-floating-label + label.floating-label, input[type="color"].with-floating-label + label.floating-label, textarea.with-floating-label + label.floating-label {
  font-size: 1rem;
  color: rgba(0, 0, 0, 0.26);
  position: relative;
  top: -35px;
  transition: top .45s ease-in-out, color .45s ease-in-out, font-size .45s ease-in-out;
  height: 0;
  cursor: text;
}
input[type="text"].with-floating-label:focus + label.floating-label, input[type="text"].with-floating-label:valid + label.floating-label, input[type="password"].with-floating-label:focus + label.floating-label, input[type="password"].with-floating-label:valid + label.floating-label, input[type="date"].with-floating-label:focus + label.floating-label, input[type="date"].with-floating-label:valid + label.floating-label, input[type="datetime"].with-floating-label:focus + label.floating-label, input[type="datetime"].with-floating-label:valid + label.floating-label, input[type="datetime-local"].with-floating-label:focus + label.floating-label, input[type="datetime-local"].with-floating-label:valid + label.floating-label, input[type="month"].with-floating-label:focus + label.floating-label, input[type="month"].with-floating-label:valid + label.floating-label, input[type="week"].with-floating-label:focus + label.floating-label, input[type="week"].with-floating-label:valid + label.floating-label, input[type="email"].with-floating-label:focus + label.floating-label, input[type="email"].with-floating-label:valid + label.floating-label, input[type="number"].with-floating-label:focus + label.floating-label, input[type="number"].with-floating-label:valid + label.floating-label, input[type="search"].with-floating-label:focus + label.floating-label, input[type="search"].with-floating-label:valid + label.floating-label, input[type="tel"].with-floating-label:focus + label.floating-label, input[type="tel"].with-floating-label:valid + label.floating-label, input[type="time"].with-floating-label:focus + label.floating-label, input[type="time"].with-floating-label:valid + label.floating-label, input[type="url"].with-floating-label:focus + label.floating-label, input[type="url"].with-floating-label:valid + label.floating-label, input[type="color"].with-floating-label:focus + label.floating-label, input[type="color"].with-floating-label:valid + label.floating-label, textarea.with-floating-label:focus + label.floating-label, textarea.with-floating-label:valid + label.floating-label {
  color: #00bcd4;
  font-size: 0.75rem;
  top: -56px;
}
</style>
