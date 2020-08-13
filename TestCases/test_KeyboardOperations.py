from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os

def test_mycase():

    # Set chrome driver
    print("Set chrome driver")

    driver = webdriver.Remote(
        command_executor="http://10.200.243.162:5555/wd/hub",
        desired_capabilities={
            "browserName": "chrome",
            "browserVersion": "latest",
            "video": "True",
            "platform": "WIN10",
            "platformName": "windows",
        })

    driver.get("http://www.theTestingWorld.com/testings")
    driver.find_element_by_name("fld_username").send_keys("Hello")

    act = ActionChains(driver)
    act.send_keys(Keys.CONTROL).send_keys("a").perform()
