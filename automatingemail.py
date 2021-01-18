from config import email,password
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from gmail import subj,c_email
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



dataframe = pd.read_excel('text.xlsx')
#print(dataframe.index)



browser = webdriver.Firefox()
browser.get('https://www.gmail.com')
browser.implicitly_wait(4)
username ='input[type="email"]'
browser.find_element_by_css_selector(username).send_keys(email)
browser.find_element_by_class_name('VfPpkd-RLmnJb').click()
browser.implicitly_wait(100)
time.sleep(2)
browser.find_element_by_name('password').send_keys(password)
browser.find_element_by_class_name('VfPpkd-RLmnJb').click()
for i in dataframe.index:
    time.sleep(2)
    browser.find_element_by_css_selector('.T-I.T-I-KE.L3').click()
    time.sleep(2)
    time.sleep(3)
    r_email=dataframe.loc[i]['email']
    browser.find_element_by_name("to").send_keys(r_email)
    browser.find_element_by_name("subjectbox").send_keys(subj)
    browser.find_element_by_css_selector('.Am.Al.editable.LW-avf.tS-tW').send_keys(c_email)
    browser.find_element_by_css_selector('.T-I.J-J5-Ji.aoO.v7.T-I-atl.L3').click()
    time.sleep(3)





    #element = WebDriverWait(browser, 500).until(
   #     EC.presence_of_element_located((By.ID, "myDynamicElement"))
  





    
