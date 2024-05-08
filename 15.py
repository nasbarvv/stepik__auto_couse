from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

#Ссылка на URL
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")
browser.maximize_window()

#Ищем по CSS СЕЛЕКТОРУ кнопку для нажатия.
browser.find_element(By.CSS_SELECTOR, "button.btn").click()

#Принять confirm
confirm = browser.switch_to.alert
confirm.accept()

#Для математической формулы
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
browser.find_element(By.CSS_SELECTOR, "button.btn").click()

time.sleep (10)
browser.quit()