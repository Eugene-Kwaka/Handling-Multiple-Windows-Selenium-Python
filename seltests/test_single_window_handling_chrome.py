import os
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

def test_single_window_chrome():
    options = ChromeOptions()
    options.browser_version = '103.0'
    options.platform_name = 'Windows 10'
    lt_options = {}
    lt_options['username'] = os.environ.get ('LAMBDATEST_USER')
    lt_options['accesskey'] = os.environ.get ('LAMBDATEST_ACCESSKEY')
    lt_options['project'] = 'SingleWindowHandling'
    lt_options['selenium_version'] = '4.1.2'
    lt_options['w3c'] = True
    options.set_capability('LT:options', lt_options)
    # LambdaTest Profile username
    user_name = os.environ.get ('LAMBDATEST_USER')
    # LambdaTest Profile access_key
    accesskey = os.environ.get ('LAMBDATEST_ACCESSKEY')
    remote_url = "https://" + user_name + ":" + \
        accesskey + "@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(remote_url, options=options)
    driver.get('https://www.lambdatest.com/selenium-playground')
    driver.maximize_window()
    # Look for the window popup modal link and click
    element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="https://www.lambdatest.com/selenium-playground/window-popup-modal-demo"]')))
    element.click()
    # Get the window handle Id of the current parent window
    parent_guid = driver.current_window_handle
    print(f"The parent window guid is: {parent_guid}")
    twitter_element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[title="Follow @Lambdatesting on Twitter"]')))
    twitter_element.click()
    # Get the window handle ids of all the windows opened
    all_guid = driver.window_handles
    # iterate through the guids and if there is a parent window id skip it and switch to the new window
    for guid in all_guid:
        if guid != parent_guid:
            driver.switch_to.window(guid)
            print(f"The child guid is: {guid}")
            driver.close()

    driver.quit()

  