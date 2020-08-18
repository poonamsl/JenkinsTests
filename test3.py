from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from sauceclient import SauceClient
import os

# Retrieving environment variables
SAUCE_USERNAME = os.environ.get('SAUCE_USERNAME')
SAUCE_ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')

#sauce_client = SauceClient(SAUCE_USERNAME,SAUCE_ACCESS_KEY)

# The command_executor tells the test to run on Sauce, while the desired_capabilitues 
# parameter tells us which browsers and OS to spin up
desired_cap = {
	'platform': "Windows 10",
	'browserName': "chrome",
	'name':'test3',
	'public':'public'
}
#'version': "31",

myUrl = 'http://' + SAUCE_USERNAME + ':' + SAUCE_ACCESS_KEY + '@ondemand.saucelabs.com:80/wd/hub';
driver = webdriver.Remote (
	command_executor=myUrl,desired_capabilities=desired_cap)

# This is your test logic. You can add multiple tests here.
driver.get("https://www.google.com")

print "SauceOnDemandSessionID=" + driver.session_id + " job-name=sanity"

#driver.execute_script("sauce:job-result=passed")

# This is where you tell Sauce Labs to stop running tests on your behalf.
# It's important so that you aren't billed after your test finishes
driver.quit()
#sauce_client.jobs.update_job(driver.session_id, passed=True)
