from appium import webdriver
import os

# Retrieving environment variables
SAUCE_USERNAME = os.environ.get('SAUCE_USERNAME')
SAUCE_ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')

caps = {
  'browserName': 'Chrome',
  'platformVersion': '10',
  'platformName': 'Android',
  'name': 'Jenkins Test'
}

myUrl = 'https://' + SAUCE_USERNAME + ':' + SAUCE_ACCESS_KEY + '@ondemand.us-west-1.saucelabs.com:443/wd/hub';
driver = webdriver.Remote (
	command_executor=myUrl,desired_capabilities=caps)

driver.get("https://www.google.com")

session_url = driver.desired_capabilities['testobject_test_report_url']
session_id = session_url.split("/")[4]
print "SauceOnDemandSessionID=" + session_id + " job-name=Jenkins Test"

driver.execute_script("sauce:job-result=passed")

driver.quit()
