from selenium import webdriver
import math
import time

from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")
browser.maximize_window()

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)

browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()

browser.find_element(By.ID, 'robotsRule').click()

browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

time.sleep(30)
browser.quit()
