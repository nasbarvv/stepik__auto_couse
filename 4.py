from selenium import webdriver
from selenium.webdriver.common.by import (By)
from faker import Faker
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    # Создаем объект Faker
    fake = Faker()

    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        # Генерируем случайные данные в зависимости от типа поля
        if element.get_attribute("name") == "firstname":
            element.send_keys(fake.first_name())
        elif element.get_attribute("name") == "lastname":
            element.send_keys(fake.last_name())
        elif element.get_attribute("name") == "email":
            element.send_keys(fake.email())
        else:
            # Для остальных полей генерируем случайные слова
            element.send_keys(fake.word())

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла



