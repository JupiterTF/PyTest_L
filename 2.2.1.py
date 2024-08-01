from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import math

# URL страницы
link = "https://suninjuly.github.io/selects1.html"

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

    x_element = browser.find_element(By.ID, 'num1')
    x = x_element.text
    y_element = browser.find_element(By.ID, 'num2')
    y = y_element.text
    z = int(x) + int(y)
    z = str(z)

# Заполнение формы
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(z)




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
    time.sleep(5)
    if 'browser' in locals():
        browser.quit()
