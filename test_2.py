from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

text = str(math.ceil(math.pow(math.pi, math.e)*10000))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_link_text")
browser.find_element(By.XPATH, "//a[contains(text(), " + text + ")]").click()

browser.find_element(By.TAG_NAME, "input").send_keys("Maksim")

browser.find_element(By.NAME, 'last_name').send_keys("Gamov")

browser.find_element(By.CLASS_NAME, "city").send_keys("Penza")

browser.find_element(By.ID, 'country').send_keys("Russia")

browser.find_element(By.CSS_SELECTOR, "button.btn").click()

time.sleep(30)
browser.quit()



