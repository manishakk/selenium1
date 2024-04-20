import pytest
import allure
import time
from selenium import *
from allure_commons.types import AttachmentType

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# ("augtest_040823@idrive.com")
# self.log.info("Enter the Password")
# self.hp.Enter_Password("123456")

@allure.feature("Verify url")
@allure.title("Verify login functionality")
def test_url():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")
    assert driver.current_url == "https://www.idrive360.com/enterprise/login", "Incorrect url"

    username = driver.find_element(By.XPATH, "//input[@id='username']")
    username.send_keys("augtest_040823@idrive.com")
    password = driver.find_element(By.XPATH, "//input[@id='password']")
    password.send_keys("123456")
    sign_in = driver.find_element(By.XPATH, "//button[@type='submit']")
    sign_in.click()
    time.sleep(5)

    textmessage = driver.find_element(By.XPATH, "//h5[@class='id-card-title']").text
    print(textmessage)
    assert textmessage == "Your free trial has expired", "Invalid message"

    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true", "Incoorect_trialpage_url"

    allure.attach(driver.get_screenshot_as_png(), name='Trial_message_Screenshot', attachment_type=AttachmentType.PNG)


