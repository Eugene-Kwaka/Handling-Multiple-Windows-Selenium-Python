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
    lt_options['username'] = '<username>'
    lt_options['accesskey'] = '<accesskey>'
    lt_options['project'] = 'Multiple Window Handling Test'
    lt_options['selenium_version'] = '4.0.0'
    lt_options['w3c'] = True
    options.set_capability('LT:options', lt_options)
    # LambdaTest Profile username
    user_name = "<username>"
    # LambdaTest Profile access_key
    accesskey = "<accesskey>"
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
    print(f"The parent window handle is: {parent_guid}")
    # Locate and click on the button "Follow Twitter & Facebook"
    web_element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'followboth')))
    web_element.click()
    # Get the window handle ids of all the windows opened
    all_guid = driver.window_handles
    # iterate through the guids and if there is a parent window id skip it and switch to the new window
    for guid in all_guid:
        if guid != parent_guid:
            driver.switch_to.window(guid)
            page_title = driver.title
            print(f"The page title of child window is: {page_title}")
            if page_title == "Twitter":
                twitter_signup = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/i/flow/signup"]')))
                twitter_signup.click()
                driver.close()
            elif page_title == "Facebook":
                fb_login = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Accessible login button"]')))
                fb_login.click()
                driver.close()
            break
    
    driver.quit()
    


  