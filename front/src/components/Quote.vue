<template>
  <div class="quote">
      <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" class="sr-only">
          <symbol id="icon-twitter" viewBox="0 0 24 24">
              <path d="M23.954 4.569c-.885.389-1.83.654-2.825.775 1.014-.611 1.794-1.574 2.163-2.723-.951.555-2.005.959-3.127 1.184-.896-.959-2.173-1.559-3.591-1.559-2.717 0-4.92 2.203-4.92 4.917 0 .39.045.765.127 1.124C7.691 8.094 4.066 6.13 1.64 3.161c-.427.722-.666 1.561-.666 2.475 0 1.71.87 3.213 2.188 4.096-.807-.026-1.566-.248-2.228-.616v.061c0 2.385 1.693 4.374 3.946 4.827-.413.111-.849.171-1.296.171-.314 0-.615-.03-.916-.086.631 1.953 2.445 3.377 4.604 3.417-1.68 1.319-3.809 2.105-6.102 2.105-.39 0-.779-.023-1.17-.067 2.189 1.394 4.768 2.209 7.557 2.209 9.054 0 13.999-7.496 13.999-13.986 0-.209 0-.42-.015-.63.961-.689 1.8-1.56 2.46-2.548l-.047-.02z"/>
          </symbol>
          <symbol id="icon-quote" viewBox="0 0 24 24">
              <path d="M15.14 19.86h4.72L23 13.57V4.14h-9.43v9.43h4.72M2.57 19.86h4.71l3.15-6.29V4.14H1v9.43h4.71l-3.14 6.29z"/>
          </symbol>
          <symbol id="icon-github" viewBox="0 0 24 24">
              <path d="M12 1.678c-6.075 0-11 4.925-11 11 0 4.86 3.151 8.983 7.523 10.437.55.101.75-.239.75-.529 0-.262-.01-1.129-.015-2.047-3.059.664-3.705-1.298-3.705-1.298-.501-1.27-1.222-1.608-1.222-1.608-1-.682.076-.669.076-.669 1.105.077 1.686 1.133 1.686 1.133.982 1.682 2.576 1.196 3.201.914.1-.71.385-1.196.699-1.47-2.442-.277-5.011-1.221-5.011-5.436 0-1.202.429-2.182 1.131-2.952-.112-.28-.49-1.399.109-2.913 0 0 .923-.295 3.025 1.128A10.471 10.471 0 0 1 12 6.998c.935.004 1.876.126 2.754.371 2.099-1.424 3.023-1.128 3.023-1.128.601 1.516.223 2.634.11 2.912.705.77 1.13 1.75 1.13 2.952 0 4.225-2.572 5.156-5.023 5.428.396.342.747 1.01.747 2.036 0 1.47-.015 2.656-.015 3.019 0 .292.2.635.757.527C19.851 21.658 23 17.536 23 12.678c0-6.075-4.925-11-11-11z"/>
          </symbol>
    </svg>
        <blockquote class="quoteBox">
            <p class="quoteBox__text">{{ quote.quote }}</p>
            <footer class="quoteBox__footer">
                <div class="quoteBox__footerCell quoteBox__footerCell--btnIcons">
                    <a :href="twitterUrl" class="quoteBox__tweet btnIcon btnIcon--twitter" data-js="quoteBox__tweet" title="Tweet this quote" target="_blank">
                        <svg class="btnIcon__icon">
                            <use xlink:href="#icon-twitter"/>
                        </svg>
                    </a>
                    <button type="button" v-on:click="getNewQuote" class="btnIcon btnIcon--primary" title="New quote">
                        <svg class="btnIcon__icon">
                            <use xlink:href="#icon-quote"/>
                        </svg>
          </button>
                    <a href="https://github.com/pando85/quotes-simple-web" class="btnIcon" title="Github">
                        <svg class="btnIcon__icon">
                            <use xlink:href="#icon-github"/>
                        </svg>
                    </a>
                </div>
                <div class="quoteBox__footerCell quoteBox__footerCell--author">
                    <p class="quoteBox__author">{{ quote.author }}</p>
                </div>
            </footer>
    </blockquote>
  </div>
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

  get twitterUrl() {
    return `https://twitter.com/intent/tweet?text="${this.quote.quote}" — ${this.quote.author}`;
  }

  private mounted() {
    this.$store.dispatch('getRandomQuote');
  }

private getNewQuote(event: Event): void {
    this.$store.dispatch('getRandomQuote');
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss" src="./quote.scss"></style>
