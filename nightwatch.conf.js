const seleniumServer = require("selenium-server");
const chromedriver = require("chromedriver");
const geckodriver = require("geckodriver");
const SCREENSHOT_PATH = "./screenshots/";

module.exports = {
  "src_folders": [
    "tests"
  ],
  "output_folder": "./reports",
  "selenium": {
    "start_process": true,
    "server_path": seleniumServer.path,
    "host": "127.0.0.1",
    "port": 4444,
    "cli_args": {
      "webdriver.chrome.driver" : chromedriver.path,
      "webdriver.gecko.driver" : geckodriver.path
    }
  },
  "test_settings": {
    "default": {
      "screenshots": {
        "enabled": false,
      },
      "globals": {
        "waitForConditionTimeout": 2000
      },
      "desiredCapabilities": {
        "browserName": "chrome"
      }
    },
    "chrome": {
      "desiredCapabilities": {
        "browserName": "chrome",
        "javascriptEnabled": true
      }
    },
    "firefox": {
      "desiredCapabilities": {
        "browserName": "firefox",
        "javascriptEnabled": true,
        "marionette": true
      }
    }
  }
}
