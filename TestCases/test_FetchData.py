from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec
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
    driver.refresh()
    # Maximize browser
    # driver.implicitly_wait(20)
    driver.maximize_window()
    yield
    driver.close()

def test_verify_registration(environment_setup):
    #  Work on Dropdown
    wait  = WebDriverWait(driver,100)
    wait.until(ec.text_to_be_present_in_element((By.ID,'countryId'),"India"))
    obj = Select(driver.find_element_by_id("countryId"))

    obj.select_by_visible_text("India")

    wait.until(ec.text_to_be_present_in_element((By.ID, 'stateId'), "Delhi"))
    obj = Select(driver.find_element_by_id("stateId"))
    obj.select_by_visible_text("Delhi")