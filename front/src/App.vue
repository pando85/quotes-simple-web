<template>
  <div id="app">
    <Quote/>
  </div>
</template>


<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

import Quote from '@/components/Quote.vue';

@Component({
  components: {
    Quote,
  },
})
export default class Home extends Vue {}
</script>

<style lang="scss">
#app {
	display: -webkit-box;
	display: -ms-flexbox;
	display: flex;
	-webkit-box-pack: center;
	-ms-flex-pack: center;
	justify-content: center;
	-webkit-box-align: center;
	-ms-flex-align: center;
	align-items: center;
	min-height: 100vh;
	padding: 0.5rem;
}
</style>
