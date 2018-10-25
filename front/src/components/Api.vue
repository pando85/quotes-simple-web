<template>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import store from '@/store.ts';
import axios, { AxiosRequestConfig, AxiosPromise } from 'axios';

@Component
export default class Api extends Vue {
  public store!: object;
  private apiUrl: object = this.$store.state.apiUrl;

  private async mounted() {
    const response = await axios.get(`${this.apiUrl}/quotes/random`);

    return this.$store.state.quote = response.data;
  }
}
</script>
