<!-----quote and image card component---->
<template>
  <div class='card'>
    <div class="quote-text-wrap">
      <p class='quote-text'>{{ quote }}</p>
      <!--using the button component-->
      <ButtonComponent classname='download-button' buttonText='Download'
:handleClick='convertCanvasToPng'/>
      <ButtonComponent classname='copy-button'
        buttonText='Copy Quote'
        v-clipboard:copy="quote"
        :handleClick="onCopy"
        v-clipboard:error="onError"/>
    </div>
  </div>
</template>
<script>
// importing button component
import Vue from 'vue';
import VueClipboard from 'vue-clipboard2';
import ButtonComponent from '../ButtonComponent/Button.vue';

Vue.use(VueClipboard);

export default {
  name: 'QuoteComponent',
  components: {
    ButtonComponent,
  },
  props: { quote: String, classname: String, order: Number },
  data() {
    return {
      // copiedQuote: '',
    };
  },
  methods: {
    /* function to print quote in canvas and then convert it
into png file with given properties in the task. */
    convertCanvasToPng() {
      const canvas = document.createElement('canvas');
      const ctx = canvas.getContext('2d');
      canvas.width = 1080;
      canvas.height = 250;
      const maxWidth = 400;
      const lineHeight = 25;
      const x = 500;
      const y = 40;
      ctx.font = '800 18px Arial';
      ctx.textAlign = 'center';
      ctx.fillStyle = 'white';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      ctx.fillStyle = 'red';
      this.wrapText(ctx, this.quote, x, y, maxWidth, lineHeight);
      const img = canvas.toDataURL('image/png');
      const link = document.createElement('a');
      link.download = `${this.order}_quote.png`;
      link.href = img;
      link.click();
    },
    /* eslint-disable no-param-reassign */
    wrapText(ctx, text, x, y, maxWidth, lineHeight) {
      const words = text.split(' ');
      let line = '';
      ctx.fillStyle = 'red';
      for (let n = 0; n < words.length; n += 1) {
        const breakLine = `${line + words[n]} `;
        const metrics = ctx.measureText(breakLine);
        const calculatedWidth = metrics.width;
        if (calculatedWidth > maxWidth && n > 0) {
          ctx.fillText(line, x, y);
          line = `${words[n]} `;
          y += lineHeight;
        } else {
          line = breakLine;
        }
      }
      ctx.fillText(line, x, y);
    },
    /* eslint-enable no-param-reassign */
    onCopy() {
      alert('You just copied the text to the clipboard');
    },
    onError() {
      alert('Failed to copy the text to the clipboard');
    },
  },
};
</script>
<style scoped>
@import './style.css';
</style>
