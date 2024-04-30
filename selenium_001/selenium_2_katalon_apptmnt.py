import time

import allure
import driver
import pytest


from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Verify URL")
@allure.title("Verify URL")
def test_openurl():
  driver = webdriver.Chrome()
  driver.get("https://katalon-demo-cura.herokuapp.com/")
  makeappt_element = driver.find_element(By.ID, "btn-make-appointment")
  makeappt_element.click()
  time.sleep(5)
  assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
  time.sleep(3)

# @allure.feature("Verify Login")
# @allure.title("Verify Login")
#def test_login():
  #username and password

  username = driver.find_element(By.ID,"txt-username")
  username.send_keys("John Doe")
  password = driver.find_element(By.ID,"txt-password")
  password.send_keys("ThisIsNotAPassword")
  click_login = driver.find_element(By.ID,"btn-login")
  click_login.click()


  #driver.implicitly_wait(5)

  element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME,"col-sm-12")))


# @allure.feature("Verify appointment")
#def test_makeappointment():
  # Make Appointment


  text_verify = driver.find_element(By.CLASS_NAME,"col-sm-12")
  print(text_verify)
  assert text_verify.text == "Make Appointment"

  #select dropdown
  dropdown = Select(driver.find_element(By.ID, "combo_facility"))
  dropdown.select_by_visible_text("Hongkong CURA Healthcare Center")

  #click checkbox

  driver.find_element(By.ID,"chk_hospotal_readmission").click()
  driver.find_element(By.ID, "radio_program_medicaid").click()
  driver.find_element(By.ID,"txt_visit_date").send_keys("12/05/2024")
  driver.find_element(By.ID,"txt_comment").send_keys(" I have cough")
  driver.find_element(By.ID,"btn-book-appointment").click()

  time.sleep(5)

  verify_confirmation = driver.find_element(By.CLASS_NAME, "col-xs-12")
  print(verify_confirmation)
  assert verify_confirmation.text == ("Appointment Confirmation\n"
                                      "Please be informed that your appointment has been booked as following:")
  #driver.find_element(by=By.ID, "q").send_keys("")

  #driver.find_element(self, by=By.CLASS_NAME, "gLFyf").send_keys("hi")
