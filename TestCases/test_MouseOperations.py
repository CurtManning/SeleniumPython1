from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os

def test_mouseOperations():

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
    driver.get("http://www.theTestingWorld.com/")
    act = ActionChains(driver)

    # Click operation
    #act.click().perform()
    #act.click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

    # Context Click(Right Click)
    #act.context_click().perform()
    #act.context_click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

    #act.double_click().perform()
    #act.double_click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

    act.move_to_element(driver.find_element_by_xpath("//span[contains(text(),'TUTORIAL')]")).perform()

