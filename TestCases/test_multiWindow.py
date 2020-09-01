from selenium import webdriver
import time
import pytest
import os

@pytest.fixture()
def environment_setup():
    global driver
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
    driver.maximize_window()
    yield
    driver.close()

def test_verify_registration(environment_setup):
    driver.find_element_by_xpath("//label[text()='Login']").click()
    driver.find_element_by_name("_txtUserName").send_keys("test")
    driver.find_element_by_name("_txtPassword").send_keys("test")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()
    driver.find_element_by_xpath("//a[contains(text(),'My Account')]").click()
    driver.find_element_by_xpath("//a[contains(text(),'Update')]").click()
    time.sleep(10)
    allwindows = driver.window_handles
    mainWin = ""
    for win in allwindows:
        driver.switch_to.window(win)
        if driver.current_url == 'http://www.thetestingworld.com/testings/manage_customer.php':
            driver.find_element_by_xpath("//button[text()='Start Download']").click()
            time.sleep(5)
            driver.close()
        elif driver.current_url == 'http://www.thetestingworld.com/testings/dashboard.php':
            mainWin = win

    driver.switch_to.window(mainWin)
    print(driver.current_url)
