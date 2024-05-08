from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.get(link)

# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
home_price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

if home_price:
    # Нажать на кнопку "Book"
    browser.find_element(By.ID, 'book').click()

#Решить математическую задачу и отправить решение
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

element = browser.find_element(By.ID, 'input_value')
x_element = element.text
captcha = calc(int(x_element))
browser.find_element(By.ID, 'answer').send_keys(str(captcha))
browser.find_element(By.ID, 'solve').click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
