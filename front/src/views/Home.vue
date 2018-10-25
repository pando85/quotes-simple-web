<template>
  <div class="home">
    <Quote/>
    <Api/>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

import Api from '@/components/Api.vue';
import Quote from '@/components/Quote.vue';

@Component({
  components: {
    Api,
    Quote,
  },
})
export default class Home extends Vue {}
</script>
