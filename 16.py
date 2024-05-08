from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

#Открывает ссылку
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")
browser.maximize_window() #Открывает на весь экран

#Нажимает на кнопку
browser.find_element(By.CSS_SELECTOR, "button.btn").click()

#
confirm = browser.switch_to.alert
confirm.accept()

#открывает новую вкладку
browser.switch_to.window(window_name)

