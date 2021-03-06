from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from sauceclient import SauceClient
import os


# Retrieving environment variables
SAUCE_USERNAME = os.environ.get('SAUCE_USERNAME')
SAUCE_ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')
#SELENIUM_PLATFORM = "OS X 10.11"
#SELENIUM_BROWSER = "chrome"

#sauce_client = SauceClient(SAUCE_USERNAME,SAUCE_ACCESS_KEY)

# The command_executor tells the test to run on Sauce, while the desired_capabilitues 
# parameter tells us which browsers and OS to spin up
desired_cap = {
	'platform': "Mac OS X 10.13",
	'browserName': "chrome",
	'name':'test1',
	'version': "latest",
}
#'version': "31",

#SELENIUM_PLATFORM, SELENIUM_VERSION, and SELENIUM_BROWSER 
#desired_cap = {}
#deviceType = os.environ.get('SELENIUM_DEVICE_TYPE')
#print "abc"
#print deviceType
#platform = os.environ.get('SELENIUM_PLATFORM')
#if platform == "android":
#	desired_cap['deviceName'] = os.environ.get('SELENIUM_DEVICE')
#else:
#	desired_cap['platform'] = platform
#desired_cap['browserName'] = os.environ.get('SELENIUM_BROWSER')
#desired_cap['name'] = 'test1'
#desired_cap['version'] = os.environ.get('SELENIUM_VERSION')
#desired_cap['build'] = 'mybuild'
#desired_cap['public'] = 'public restricted'


myUrl = 'http://' + SAUCE_USERNAME + ':' + SAUCE_ACCESS_KEY + '@ondemand.saucelabs.com:80/wd/hub';
driver = webdriver.Remote (
	command_executor=myUrl,desired_capabilities=desired_cap)

# This is your test logic. You can add multiple tests here.
driver.implicitly_wait(10)
driver.get("http://www.google.com")
if not "Google" in driver.title:
	raise Exception("Unable to load google page!")
	driver.execute_script("sauce:job-result=failed")
	
elem = driver.find_element_by_name("q")
elem.send_keys("Sauce Labs")
elem.submit()
#print driver.title

# Insert a break point to take manual control of the browser 
# through the test's live window

#driver.execute_script("sauce: break")
#print driver.session_id
print "SauceOnDemandSessionID=" + driver.session_id + " job-name=test1"
print "SauceOnDemandBrowsers=" + os.environ.get('SAUCE_ONDEMAND_BROWSERS')
#print "Platform " + os.environ.get('SELENIUM_PLATFORM')
#print "Browser" + os.environ.get('SELENIUM_BROWSER')
#printenv

driver.execute_script("sauce:job-result=passed")

# This is where you tell Sauce Labs to stop running tests on your behalf.
# It's important so that you aren't billed after your test finishes
driver.quit()

#sauce_client.jobs.update_job(driver.session_id, passed=True)
