from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

# URL страницы
link = "https://suninjuly.github.io/get_attribute.html"

# Вычисление текста ссылки
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Инициализация браузера с использованием Service
    service = Service('C:/chromedriver/chromedriver.exe') 
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=service, options=options)

     # Открытие страницы
    browser.get(link) 
#treasure
    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)

# Заполнение формы
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None
    
  # Клик по чекбоксу 
    CheckBox1 = browser.find_element(By.ID, "robotCheckbox")
    CheckBox1.click()
  # Клик по Радиобатону 
    RadioB = browser.find_element(By.ID, "robotsRule")
    RadioB.click()





 # Клик по кнопке
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

        # Ожидание алерта, чтобы успеть скопировать код
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)  # Вывод текста алерта для проверки
finally:
        # Закрываем браузер после всех манипуляций
    time.sleep(10)
    if 'browser' in locals():
        browser.quit()