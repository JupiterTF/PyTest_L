import math
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, 'input')
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser
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
    time.sleep(3)
    if 'browser' in locals():
        browser.quit()
