from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from sauceclient import SauceClient
import os
import json

# Retrieving environment variables
SAUCE_USERNAME = os.environ.get('SAUCE_USERNAME')
SAUCE_ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')

sauce_client = SauceClient(SAUCE_USERNAME,SAUCE_ACCESS_KEY)
myUrl = 'http://' + SAUCE_USERNAME + ':' + SAUCE_ACCESS_KEY + '@ondemand.saucelabs.com:80/wd/hub';

SauceOnDemandBrowsers_String = os.environ.get('SAUCE_ONDEMAND_BROWSERS')
parsed_json = json.loads(SauceOnDemandBrowsers_String)

num = len(parsed_json)
for i in range(num):
	currentCaps = parsed_json[i]
	
	# The command_executor tells the test to run on Sauce, while the desired_capabilitues 
	# parameter tells us which browsers and OS to spin up
	desired_cap = {
		'platform': currentCaps['os'],
		'browserName': currentCaps['browser'],
		'version': currentCaps['browser-version'],
		'name':'test7',
		'public':'public'
		'build':'daily_build #10'
	}

	driver = webdriver.Remote(command_executor=myUrl,desired_capabilities=desired_cap)
	driver.get("http://www.google.com")
	print "SauceOnDemandSessionID=" + driver.session_id + " job-name=test7"
	driver.quit()
	sauce_client.jobs.update_job(driver.session_id, passed=True)
