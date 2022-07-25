import pytest
from selenium import webdriver
import sys
from selenium.webdriver.common.by import By

driver_capabilities = {
    "single_test": {
	"browserName": "Firefox",
	"browserVersion": "102.0",
	"LT:Options": {
		"username": "<username>",
		"accessKey": "<accesskey>",
		"platformName": "Windows 10",
		"build": "MultipleWindowHandlingSeleniumPython",
		"project": "multiwindowhandling",
		"name": "SingleWindowHandling",
		"selenium_version": "4.0.0",
		"w3c": True
	}
    }
}


def test_single_window_firefox():
    # LambdaTest Profile username
    user_name = "<username>"
    # LambdaTest Profile access_key
    accesskey = "<accesskey>"
    remote_url = "https://" + user_name + ":" + accesskey + "@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(command_executor=remote_url, desired_capabilities=driver_capabilities)
    driver.get('https://www.lambdatest.com/selenium-playground')
    driver.maximize_window()
    parent_guid = driver.current_window_handle
    print(parent_guid)



