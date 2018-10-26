import Vuex from 'vuex';
import { createLocalVue, shallowMount } from '@vue/test-utils';

import Quote from '@/components/Quote.vue';

const localVue = createLocalVue();
localVue.use(Vuex);

describe('Quote.vue', () => {
  let actions;
  let store!: any;
  const quote = { author: 'Foo', quote: 'Lorem Ipsum'};

  beforeEach(() => {
    actions = {
      getRandomQuote: jest.fn()
    };
    store = new Vuex.Store({
      state: {
        quote: quote
      },
      actions,
    });
  });

  it('renders state.quote when passed', () => {
    const wrapper = shallowMount(Quote, {
      localVue,
      store,
    });
    expect(wrapper.text()).toMatch(quote.quote);
    expect(wrapper.text()).toMatch(quote.author);
  });
});
