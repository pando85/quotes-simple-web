module.exports = {
    'Test basic function' : function (browser) {
      let quotesWeb = browser.url('http://localhost')
        .waitForElementVisible('body', 1000)
        .waitForElementVisible('a[name="new_quote"]', 1000)
        .click('a[name="new_quote"]')
        .pause(50);
      quotesWeb.expect.element('p[name="quote"]').text.to.not.equal('');
      quotesWeb.expect.element('p[name="author"]').text.to.not.equal('');
      quotesWeb.end();
    }
  };
