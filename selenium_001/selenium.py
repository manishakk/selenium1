import pytest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def test_opengoogle():
  driver = webdriver.Chrome()
  driver.get("http://google.com")
  driver.maximize_window()
  #hi
  #driver.find_element(by=By.ID, "q").send_keys("")

  #driver.find_element(self, by=By.CLASS_NAME, "gLFyf").send_keys("hi")
