import pytest
from selenium import webdriver
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService


# driver_capabilities = {
#   "single_test": {
# 	"browserName": "Chrome",
# 	"browserVersion": "103.0",
# 	"LT:Options": {
# 		"username": "kwakaeugene",
# 		"accessKey": "3zjuBwGkr45Cnf3BOHxiFFnoFonRSWdynHHLgN7HnZUJjMDaBD",
# 		"platformName": "Windows 10",
# 		"project": "Untitled",
# 		"selenium_version": "4.0.0",
# 		"w3c": True,
# 		"plugin": "python-pytest"
# 	}
#   }
# }

options = ChromeOptions()
options.browser_version = "103.0"
options.platform_name = "Windows 10"
lt_options = {};
lt_options["username"] = "<user_name>";
lt_options["accessKey"] = "<accesskey>";
lt_options["resolution"] = "1280x1024";
lt_options["headless"] = True;
lt_options["seCdp"] = True;
lt_options["build"] = "MultipleWindowHandlingSeleniumPython";
lt_options["project"] = "MultipleWindowHandling";
lt_options["name"] = "SingleWindowHandling";
lt_options["selenium_version"] = "4.0.0";
lt_options["driver_version"] = "103.0";
lt_options["w3c"] = True;
lt_options["plugin"] = "python-python";
options.set_capability('LT:Options', lt_options);


def test_single_window_chrome():
    # LambdaTest Profile username
    user_name = "<user_name>"
    # LambdaTest Profile access_key
    accesskey = "<accesskey>"
    remote_url = "https://" + user_name + ":" + accesskey + "@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(
        command_executor=remote_url, desired_capabilities=driver_capabilities)
    driver.get('https://www.lambdatest.com/selenium-playground')
    driver.maximize_window()
    parent_guid = driver.current_window_handle
    print(parent_guid)

