<template>
  <div class="quote">
    <h1>{{ quote.author }}</h1>
    <p>{{ quote.quote }}</p>
  </div>
</template>

<script lang="ts">
import store from '@/store.ts';
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class Quote extends Vue {
  public store!: object;

  get quote() {
      return this.$store.state.quote;
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
