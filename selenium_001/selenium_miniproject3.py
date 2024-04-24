import time
import pytest
import allure
from selenium import *
from allure_commons.types import AttachmentType

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_miniproject():
    driver = webdriver.Chrome()
    time.sleep(5)
    driver.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")
    driver.maximize_window()
    #testemail = driver.find_element(By.XPATH, "//input[@id='email']")
    testemail = driver.find_element(By.ID, "email")
    testemail.send_keys("abc@gmail.com")
    time.sleep(10)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("123456")
    time.sleep(10)
    driver.find_element(By.XPATH, "//input[@id='password2']").send_keys("123456")
    time.sleep(10)
    driver.find_element(By.XPATH, "//button").click()
    time.sleep(10)
    verify_text = driver.find_element(By.XPATH, "//small").text
    time.sleep(10)
    print(verify_text)

    assert verify_text == "Username must be at least 3 characters", "Invalid message"
