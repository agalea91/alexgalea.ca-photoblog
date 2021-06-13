<template>
  <div id="bmc-wbtn">
    <!-- <script type="application/javascript" defer src="https://cdnjs.buymeacoffee.com/1.0.0/widget.prod.min.js" data-id="alexgalea" data-description="Support me on Buy me a coffee!" data-message="These photos and stories hold deep meaning to me, and I hope they had an impact on you too. Thanks for your support!" data-color="#79D6B5" data-position="Right" data-x_margin="18" data-y_margin="18" data-name="BMC-Widget" data-cfasync="false"></script> -->
  </div>
</template>

<script>
export default {
  name: 'BuyMeCoffee',
  props: {},
  mounted () {
    let coffeeScript = document.createElement('script')
    coffeeScript.setAttribute('src', 'https://cdnjs.buymeacoffee.com/1.0.0/widget.prod.min.js')
    coffeeScript.setAttribute('data-id', 'alexgalea')
    coffeeScript.setAttribute('data-description', 'Support me on Buy me a coffee!')
    coffeeScript.setAttribute('data-message', 'These photos and stories hold deep meaning to me, and I hope they had an impact on you too. Thanks for your support!')
    coffeeScript.setAttribute('data-color', '#79D6B5')
    coffeeScript.setAttribute('data-position', 'Right')
    coffeeScript.setAttribute('data-x_margin', '18')
    coffeeScript.setAttribute('data-y_margin', '18')
    coffeeScript.setAttribute('data-name', 'BMC-Widget')
    coffeeScript.setAttribute('data-cfasync', 'false')
    document.head.appendChild(coffeeScript)
  }
}
</script>
