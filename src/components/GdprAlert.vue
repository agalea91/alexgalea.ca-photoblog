<template>
  <transition name="fade">
    <div class="modal" v-if="show">
      <div id="gdpr-alert">
        By browsing this site you consent to our <a href="/cookies-policy">Cookies Policy</a>
        <button type="button" class="modal-button" @click="closeModal()">
          <svg class="modal-x-svg" xmlns="http://www.w3.org/2000/svg" viewBox="-25 -25 80 80" width="50" overflow="visible" stroke="black" stroke-width="10" stroke-linecap="round">
            <line x1="0" y1="0" x2="50" y2="50" />
            <line x1="50" y1="0" x2="0" y2="50" />
          </svg>
        </button>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: 'GdprAlert',
  data () {
    return {
      show: true
    }
  },
  methods: {
    closeModal () {
      this.show = false
      document.querySelector('body').classList.remove('overflow-hidden')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}

.modal-button {
  border: 0px;
  background: white;
  :hover {
    cursor: pointer;
  }
}

.modal-x-svg {
  width: 10px;
  height: auto;
}

</style>
