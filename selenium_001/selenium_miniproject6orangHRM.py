import pytest
import allure
import time
from selenium import *
from allure_commons.types import AttachmentType

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import by

@allure.feature("Verify url")
@allure.title("Verify ebay")
def test_url():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", "Incorrect url"

    time.sleep(5)
    # ername us= driver.find_element(By.XPATH, "//input[@name='username']")
    username = driver.find_element(By.NAME, "username")
    time.sleep(2)

    username.send_keys("Admin")
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    time.sleep(2)
    password.send_keys("admin123")

    click_login = driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")
    click_login.click()
    time.sleep(2)

    click_admin = driver.find_element(By.XPATH,"//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][text()[contains(.,'Admin')]]")
    click_admin.click()

    time.sleep(2)


    click_addusers = driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
    click_addusers.click()

    time.sleep(2)

    clickdropdown = driver.find_element(By.XPATH,"//div[@class='oxd-select-text oxd-select-text--active']")
    clickdropdown.click()

    time.sleep(1)

    driver.find_element(By.XPATH, "(//div[@role='listbox']//child::div)[1]").click()
    time.sleep(2)

   #enter name
    driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys("monty")

    time.sleep(1)

    #enter sttatus   oxd-select-text oxd-select-text--active



    driver.quit()



########################################################

