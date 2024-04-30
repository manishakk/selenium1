import pytest
import allure
import time
from selenium import *
from allure_commons.types import AttachmentType
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_emailcreation():
    response = requests.get(url="https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1",
                                auth=None
                                )


    email_id = response.json()
    print(email_id)

def test_message():
    response = requests.get(url="https://www.1secmail.com/api/v1/?action=getMessages&login=email_id&domain=1secmail.com")
    get_message = response.json()
    print(get_message)

