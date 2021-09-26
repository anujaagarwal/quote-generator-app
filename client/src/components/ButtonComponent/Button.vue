<!----Button Component----->
<template>
  <div>
    <button :class="classname" v-on:click="handleClick" :disabled="disabled">{{buttonText}}</button>
  </div>
</template>
<script>
export default {
  name: 'ButtonComponent',
  props: {
    buttonText: String, handleClick: Function, classname: String, disabled: Boolean,
  },
};
</script>
<style>
/* space to style the ButtonComponent */
</style>
