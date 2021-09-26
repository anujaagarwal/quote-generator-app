<!--parent component--->
<template>
  <div id="app">
    <RandomQuotesComponent/>
  </div>
</template>
<script>
/* importing the requirements */
import RandomQuotesComponent from './views/RandomQuotes.vue';

export default {
  name: 'App',
  components: {
    RandomQuotesComponent,
  },
};
</script>
<style>
  /* we can style our app component */
</style>
