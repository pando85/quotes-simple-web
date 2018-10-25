<template>
  <div class="home">
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
