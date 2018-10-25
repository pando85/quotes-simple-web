import { shallowMount } from '@vue/test-utils';
import quote from '@/components/quote.vue';

describe('quote.vue', () => {
  it('renders props.msg when passed', () => {
    const msg = 'new message';
    const wrapper = shallowMount(quote, {
      propsData: { msg },
    });
    expect(wrapper.text()).toMatch(msg);
  });
});
