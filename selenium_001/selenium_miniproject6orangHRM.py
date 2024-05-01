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

    driver.maximize_window()
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
#select ESS from dropdown
    clickdropdownlist = driver.find_elements(By.XPATH,"//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']")
    #empnamedropdown  = clickdropdownlist[0]
    #print(empnamedropdown.text)
    clickdropdownlist[0].click()

    driver.find_element(By.XPATH, "(//div[@role='listbox']//div)[3]").click()

   # clickdropdown.click()

    time.sleep(3)
    #
    # driver.find_element(By.XPATH, "(//div[@role='listbox']//child::div)[2]").click()
    # time.sleep(2)

   #enter emplyee name

    usernames = driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']")
    usernames.send_keys("an")

    time.sleep(4)

    selectname = driver.find_element(By.XPATH, "(//div[@role='listbox']//child::div)[1]")
    selectname.click()


    # username = usernames[2]
    # username.click()


    time.sleep(1)

    #enter sttatus

    statusdropdownlist = driver.find_elements(By.XPATH,
                                            "//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']")
  #  statusdropdown = statusdropdownlist[1]
    statusdropdownlist[1].click()

    #driver.find_element(By.XPATH, "(//div[@role='listbox']//child::div)[2]").click()

    driver.find_element(By.XPATH, "(//div[@role='listbox']//div)[2]").click()
    time.sleep(2)

    #enterusername
    usernames = driver.find_elements(By.XPATH, "//input[@class='oxd-input oxd-input--active']")
    username = usernames[1]
    username.send_keys("montyuser")

    # time.sleep(1)
    #
    # username = usernames[1]
    # username.click()

    time.sleep(2)
    # password_list = driver.find_elements(By.XPATH, "//input[@class='oxd-input oxd-input--active'][@type='password'][@autocomplete='off']")
    # password_input = password_list[0]
    # repassword_input = password_list[1]
    # password_input.send_keys("admin1234")
    # repassword_input.send_keys("admin1234")

    # password
    password = driver.find_elements(By.XPATH,
                                    "//input[@class='oxd-input oxd-input--active'][@type='password'][@autocomplete='off']")
    password[0].send_keys("Test@123")
    password[1].send_keys("Test@123")

    time.sleep(2)
    #click save
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.quit()



########################################################

