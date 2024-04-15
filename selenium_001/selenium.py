import time

import driver
import pytest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def test_opengoogle():
  driver = webdriver.Chrome()
  driver.get("https://katalon-demo-cura.herokuapp.com/")
  makeappt_element = driver.find_element(By.ID, "btn-make-appointment")
  makeappt_element.click()
  time.sleep(5)
  assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
  time.sleep(3)

  #username and password
  username = driver.find_element(By.ID, "txt-username")
  username.send_keys("John Doe")
  password = driver.find_element(By.ID, "txt-password")
  password.send_keys("ThisIsNotAPassword")
  click_login = driver.find_element(By.ID, "btn-login")
  click_login.click()
  time.sleep(5)
  # Make Appointment
  page_title = driver.title
  print(page_title)

  text_verify = driver.find_element(By.CLASS_NAME,"col-sm-12")
  print(text_verify)
  assert text_verify.text == "Make Appointment"

  #hi
  #driver.find_element(by=By.ID, "q").send_keys("")

  #driver.find_element(self, by=By.CLASS_NAME, "gLFyf").send_keys("hi")
