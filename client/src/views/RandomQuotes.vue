<template>
  <!---the view is divided into one button component and number of QuoteComponent---->
  <div class='overall-view'>
    <img src="../assets/tree.gif">
    <!---Getting data from getQuotes and that data is flown from button
    component to QuoteComponent----->
      <ButtonComponent classname='button' buttonText="Generate Quotes"
:handleClick="getQuotes" :disabled="loading"/>
      <my-loader name="ball-clip-rotate-pulse" color="black" scale="2" v-if="loading"
class="loader-style"/>
      <!-- browser side error handling -->
      <div class="error-handle">{{ err }}</div>
      <QuoteComponent classname='full-list' v-for="quote in quotes" :key='quote.id'
    :quote='quote.message' :order='quote.id'/>
  </div>
</template>
<script>
// Importing the requirements
import axios from 'axios';
import Vue from 'vue';
import VueLoaders from 'vue-loaders';
import 'vue-loaders/dist/vue-loaders.css';
import ButtonComponent from '../components/ButtonComponent/Button.vue';
import QuoteComponent from '../components/QuoteComponent/QuoteCard.vue';
import config from '@/config';

Vue.component('my-loader', VueLoaders.component);

export default {
  name: 'RandomQuotesComponent',
  props: [],
  data() {
    return {
      quotes: [],
      err: '',
      loading: false,
    };
  },
  components: {
    ButtonComponent,
    QuoteComponent,
  },
  methods: {
    // using axios we are making HTTP GET request
    getQuotes() {
      this.loading = true;
      this.quotes = [];
      this.err = '';
      const path = `${config.apiUrl}/quotes/random?offset=10`;
      axios.get(path)
        .then((res) => {
          if (res.data.success) {
            this.quotes = res.data.items;
          } else { this.err = res.data.error; }
          this.loading = false;
        })
        .catch(() => {
          this.loading = false;
          this.err = 'Found an undefined error';
        });
    },
  },
};
</script>
<style scoped>
  /* all styling is imported here */
  @import './style.css';
</style>
