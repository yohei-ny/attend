import os
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager 
import os
from os.path import join, dirname
from dotenv import load_dotenv
#from att import attend
#load_dotenv()


options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.get(URL)
sleep(3)
def attend():
  click_bottan =driver.find_element_by_class_name("attendance-button-email")
  click_bottan.click()
  company_id =driver.find_element_by_id("employee_session_form_office_account_name")
  company_id.send_keys(COMAPANY)
  email_id =driver.find_element_by_id("employee_session_form_account_name_or_email")
  email_id.send_keys(MAIL)
  passwd_id =driver.find_element_by_id("employee_session_form_password")
  passwd_id.send_keys(PASSWOED)
  sleep(3)
  search_box = driver.find_element_by_name("commit")
  search_box.submit()
  sleep(3)
  bot =driver.find_element_by_xpath("//*[@id='kt-attendance-card-time-stamp']/ul/li[1]/form/a")
  driver.quit()
# input_num =int(input())
attend()
# attend =attend(os.getenv('URL'))
