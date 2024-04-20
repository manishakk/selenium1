import allure
import pytest


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@allure.feature("Verify")
def test_register():
    driver = webdriver.Chrome()
    driver.get("https://www.hyrtutorials.com/p/add-padding-to-containers.html")
    firstname = driver.find_element(By.XPATH, '//input[@name="name"]')
    firstname.send_keys("mani")
    lastname = driver.find_element(By.XPATH, '//input[@name="name"]')

