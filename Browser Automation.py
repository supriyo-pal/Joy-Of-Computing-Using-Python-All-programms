# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 21:04:47 2020

@author: Supriyo
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# browser=webdriver.Chrome("C:\\Users\Supriyo\.spyder-py3\joy of computing using python\chromedriver") 

# browser.get("https://www.seleniumhq.org")

# element=browser.find_element_by_link_text('Downloads')
# element.click()
# search=browser.find_element_by_id('q')
# search.send_keys('Sassy supriyo')

driver=webdriver.Chrome("C:\\Users\Supriyo\.spyder-py3\joy of computing using python\chromedriver")

driver.get("https://web.whatsapp.com/")
wait=WebDriverWait(driver,600)

target='"Sonam (Gec)"'
string="Message sent using Python!!!"
x_arg='//span[contains(@title, '+target + ')]'
target=wait.until(ec.presence_of_element_located((By.XPATH,x_arg)))
target.click()

input_box=driver.find_element_by_class_name('DuUXI')
for i in range(1000):
    input_box.send_keys(string+Keys.ENTER)