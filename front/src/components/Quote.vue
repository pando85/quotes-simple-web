<template>
  <v-touch v-on:swipeleft="getNewQuote" v-bind:swipe-options="{ direction:'horizontal', threshold: 50 }" class="quote">
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" class="sr-only">
      <symbol id="icon-play" viewBox="4 4 24 24" transform="scale(1.5)">
        <path d="M8 5v14l11-7z"/>
      </symbol>
      <symbol id="icon-quote" viewBox="2 2 14 14">
        <path d="M9 13.5c-2.49 0-4.5-2.01-4.5-4.5S6.51 4.5 9 4.5c1.24 0 2.36.52 3.17 1.33L10 8h5V3l-1.76 1.76C12.15 3.68 10.66 3 9 3 5.69 3 3.01 5.69 3.01 9S5.69 15 9 15c2.97 0 5.43-2.16 5.9-5h-1.52c-.46 2-2.24 3.5-4.38 3.5z"/>
      </symbol>
      <symbol id="icon-github" viewBox="0 0 24 24">
        <path d="M12 1.678c-6.075 0-11 4.925-11 11 0 4.86 3.151 8.983 7.523 10.437.55.101.75-.239.75-.529 0-.262-.01-1.129-.015-2.047-3.059.664-3.705-1.298-3.705-1.298-.501-1.27-1.222-1.608-1.222-1.608-1-.682.076-.669.076-.669 1.105.077 1.686 1.133 1.686 1.133.982 1.682 2.576 1.196 3.201.914.1-.71.385-1.196.699-1.47-2.442-.277-5.011-1.221-5.011-5.436 0-1.202.429-2.182 1.131-2.952-.112-.28-.49-1.399.109-2.913 0 0 .923-.295 3.025 1.128A10.471 10.471 0 0 1 12 6.998c.935.004 1.876.126 2.754.371 2.099-1.424 3.023-1.128 3.023-1.128.601 1.516.223 2.634.11 2.912.705.77 1.13 1.75 1.13 2.952 0 4.225-2.572 5.156-5.023 5.428.396.342.747 1.01.747 2.036 0 1.47-.015 2.656-.015 3.019 0 .292.2.635.757.527C19.851 21.658 23 17.536 23 12.678c0-6.075-4.925-11-11-11z"/>
      </symbol>
    </svg>
    <blockquote class="quoteBox" v-if="quote">
      <p class="text" name="quote">{{ quote.quote }}</p>
      <footer class="footer">
        <div class="footerCell footerCell--btnIcons">
          <a v-on:click="playAudio" class="btnIcon" name="play" title="Play audio" target="_blank">
            <svg>
              <use xlink:href="#icon-play"/>
            </svg>
          </a>
          <a v-on:click="getNewQuote" class="btnIcon" name="new_quote" title="New quote">
            <svg>
              <use xlink:href="#icon-quote"/>
            </svg>
          </a>
          <a href="https://github.com/pando85/quotes-simple-web" class="btnIcon" name="github" title="Github">
            <svg>
              <use xlink:href="#icon-github"/>
            </svg>
          </a>
        </div>
        <div class="footerCell footerCell--author">
          <p class="author" name="author">{{ quote.author }}</p>
        </div>
      </footer>
    </blockquote>
  </v-touch>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

import store from '@/store.ts';

@Component
export default class Quote extends Vue {
  public store!: object;

  get quote() {
    return this.$store.state.quote;
  }

  get apiUrl() {
    return this.$store.state.apiUrl;
  }

  get playUrl() {
    return `https://play.com/intent/tweet?text="${this.quote.quote}" — ${this.quote.author}`;
  }

  private mounted() {
    this.$store.dispatch('getRandomQuote');
  }

  private playAudio(event: Event): void {
    new Audio(`${this.apiUrl}${this.quote.audio}`).play();
  }

  private getNewQuote(event: Event): void {
    this.$store.dispatch('getRandomQuote');
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss" src="./quote.scss"></style>
