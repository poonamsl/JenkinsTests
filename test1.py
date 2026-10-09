from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from sauceclient import SauceClient
import os
from selenium.webdriver.chrome.options import Options as ChromeOptions

# Retrieving environment variables
SAUCE_USERNAME = os.environ.get('SAUCE_USERNAME')
SAUCE_ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')

options = ChromeOptions()
options.browser_version = 'latest'
options.platform_name = 'Windows 11'
sauce_options = {}
sauce_options['username'] = 'parora'
sauce_options['accessKey'] = '*****e227'
sauce_options['build'] = '<your build id>'
sauce_options['name'] = '<your test name>'
options.set_capability('sauce:options', sauce_options)

url = 'https://' + SAUCE_USERNAME + ':' + SAUCE_ACCESS_KEY + '@ondemand.saucelabs.com:443/wd/hub';
driver = webdriver.Remote(command_executor=url, options=options)

driver.get("https://www.saucedemo.com")
title = driver.title
titleIsCorrect = "Swag Labs" in title
jobStatus = "passed" if titleIsCorrect else "failed"

# end the session
driver.execute_script("sauce:job-result=" + jobStatus)

print("SauceOnDemandSessionID=" + driver.session_id + " job-name=test1")
print(f"SauceOnDemandBrowsers={os.environ.get('SAUCE_ONDEMAND_BROWSERS')}")

driver.quit()
