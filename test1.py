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


# This is your test logic. You can add multiple tests here.
driver.implicitly_wait(10)
driver.get("http://www.google.com")
if not "Google" in driver.title:
	raise Exception("Unable to load google page!")
	driver.execute_script("sauce:job-result=failed")
	
elem = driver.find_element_by_name("q")
elem.send_keys("Sauce Labs")
elem.submit()

print("SauceOnDemandSessionID=" + driver.session_id + " job-name=test1")
print("SauceOnDemandBrowsers=" + os.environ.get('SAUCE_ONDEMAND_BROWSERS'))

driver.execute_script("sauce:job-result=passed")

driver.quit()
