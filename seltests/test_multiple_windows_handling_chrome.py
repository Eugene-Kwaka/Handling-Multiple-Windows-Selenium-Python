import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_multiple_windows_chrome():
    options = ChromeOptions()
    options.browser_version = '103.0'
    options.platform_name = 'Windows 10'
    lt_options = {}
    lt_options['username'] = os.environ.get ('LT_USERNAME')
    lt_options['accesskey'] = os.environ.get ('LT_ACCESS_KEY')
    lt_options['project'] = 'Multiple Window Handling Test'
    lt_options['selenium_version'] = '4.0.0'
    lt_options['w3c'] = True
    options.set_capability('LT:options', lt_options)
    # LambdaTest Profile username
    user_name = os.environ.get ('LT_USERNAME')
    # LambdaTest Profile access_key
    accesskey = os.environ.get ('LT_ACCESS_KEY')
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
    parent_title = driver.title
    print(f"The parent window name is {parent_title} and its handle is: {parent_guid}")
    # Locate and click on the button "Follow Twitter & Facebook"
    web_element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'followboth')))
    web_element.click()
    # Get the window handle ids of all the windows opened
    all_guid = driver.window_handles
    # Get the total number of window opened.
    num_of_handles = len(all_guid)
    # print the numbers of window open.
    print(f"The number of windows open {num_of_handles} ")

    # iterate through the total number of guids and if there is a parent window id skip it and switch to the new child windows
    for num in range(num_of_handles):
        if all_guid[num] != parent_guid:
            driver.switch_to.window(all_guid[num])
            print(f"The child window's title is: {driver.title}")
            driver.close()
    
    driver.quit()
    
    
    

    


  