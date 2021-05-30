import os
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager 
import os
from os.path import join, dirname
from dotenv import load_dotenv
from att import attend
load_dotenv()

attend =attend(os.getenv('URL'))
