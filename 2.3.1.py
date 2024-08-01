import math
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# URL страницы
link = "https://suninjuly.github.io/alert_accept.html"

# Вычисление текста ссылки
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Инициализация браузера с использованием Service
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=service, options=options)
    
    # Открытие страницы
    browser.get(link)

     # Клик по кнопке
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click() 

    # Клик по алерту
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    # Заполнение формы
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    # Клик по кнопке
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Ожидание алерта, чтобы успеть скопировать код
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)  # Вывод текста алерта для проверки
    alert.accept()

finally:
    # Закрываем браузер после всех манипуляций
    if 'browser' in locals():
        browser.quit()
