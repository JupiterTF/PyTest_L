import math
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# URL страницы
link = "https://suninjuly.github.io/file_input.html"

with open("test.txt", "w") as file:
    content = file.write("automationbypython")  # create test.txt file

try:
    # Инициализация браузера с использованием Service
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=service, options=options)
    
    # Открытие страницы
    browser.get(link)
  
    # Заполнение формы
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Ivan@Petrov.ru")

    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path =  os.getcwd() + '/' + file.name           # добавляем к этому пути имя файла 
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)
    os.remove(file_path)
    
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
