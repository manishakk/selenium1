import pytest
import allure
import time
from selenium import *
from allure_commons.types import AttachmentType

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@allure.feature("Verify url")
@allure.title("Verify ebay")
def test_url():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    assert driver.current_url == "https://www.ebay.com/", "Incorrect url"

    search_text = driver.find_element(By.XPATH, "//input[@class='gh-tb ui-autocomplete-input']")
    search_text.send_keys("16 gb")
    search = driver.find_element(By.XPATH, "//input[@class='btn btn-prim gh-spr']")
    search.click()
    time.sleep(5)

    driver.implicitly_wait(5)



########################################################

    items_list = driver.find_elements(By.XPATH, "//div[@class='s-item__title']")
    for items in items_list: print(items.text)

    mylist = []
    items_pricelist = driver.find_elements(By.XPATH, "//span[@class='s-item__price']")
    print(items_pricelist)
    print("*************************")
    for prices in items_pricelist:
        #print(prices.text)
        txt = prices.text.replace("$","").strip()
        mylist.append(txt)

    print(mylist)

    print("printing sorted prices")

    mylist.sort()
    print(mylist)
    newprices = txt

    print(f"Product having: {mylist[1]}")

    # prices = sorted(txt)
    # print("Sorted Prices:", prices)


















    #allure.attach(driver.get_screenshot_as_png(), name='Trial_message_Screenshot', attachment_type=AttachmentType.PNG)


