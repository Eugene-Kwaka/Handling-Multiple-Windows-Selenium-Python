import os
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time

driver_capabilities = {
    "single_test": {
	"browserName": "Firefox",
	"browserVersion": "102.0",
	"LT:Options": {
		"username": "username",
		"accessKey": "accesskey",
		"platformName": "Windows 10",
		"build": "MultipleWindowHandlingSeleniumPython",
		"project": "multiwindowhandling",
		"name": "SingleWindowHandling",
		"selenium_version": "4.0.0",
		"w3c": True
	}
    }
}

# os.environ['PATH'] += r"C:\Program Files (x86)\Mozilla Firefox"

def test_single_window_firefox():
    options = FirefoxOptions()
    options.browser_version = '102.0'
    options.platform_name = 'Windows 10'
    lt_options = {}
    lt_options['username'] = 'username' 
    lt_options['accesskey'] = 'accesskey'
    lt_options['project'] = 'SingleWindowHandling'
    lt_options['selenium_version'] = '4.0.0'
    lt_options['w3c'] = True
    options.set_capability('LT:options', lt_options)
    
    # LambdaTest Profile username
    user_name = "username"
    # LambdaTest Profile access_key
    accesskey = "accesskey"
    remote_url = "https://" + user_name + ":" + accesskey + "@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(command_executor=remote_url, desired_capabilities=driver_capabilities, options=options)
    # # # driver = webdriver.Remote(command_executor=remote_url, options=options)
    # # driver.get('https://www.lambdatest.com/selenium-playground/window-popup-modal-demo')

    # driver = webdriver.Remote(remote_url, options=options)
    # options = webdriver.FirefoxOptions()
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # This will instantiate the webdriver class to use Firefox 
    # driver = webdriver.Firefox(options=options)
    driver.get('https://www.lambdatest.com/selenium-playground')
    driver.maximize_window()
    driver.implicitly_wait(10)
    # Look for the window popup modal link and click
    driver.find_element(By.CSS_SELECTOR, 'a[href="https://www.lambdatest.com/selenium-playground/window-popup-modal-demo"]').click()
    # driver.get('https://www.lambdatest.com/selenium-playground/window-popup-modal-demo')
    # driver.maximize_window()
    # Get the window handle Id of the current parent window
    parent_guid = driver.current_window_handle
    driver.find_element(By.CSS_SELECTOR, 'a[title="Follow @Lambdatesting on Twitter"]').click()
    # Get the window handle ids of all the windows opened
    all_guid = driver.window_handles
    # iterate through the guids and if there is a parent window id skip it and switch to the new window
    for guid in all_guid:
        if guid != parent_guid:
            driver.switch_to.window(guid)
            print(f"The child guid is: {guid}")
            break

    time.sleep(5)
    driver.quit()
    
    # driver.close()
    # # Switch back to parent window
    # driver.switch_to.window(parent_guid)
    # print(f"The parent guid is: {parent_guid}")
    

    



