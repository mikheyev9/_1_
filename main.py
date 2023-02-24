from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


#возможно указать на вашем пк где находится драйвер для взаимодействия с браузером
#path = Service(r"/home/anton/Downloads/chromedriver_linux64/chromedriver")

#список возможных опции https://peter.sh/experiments/chromium-command-line-switches/
options = webdriver.ChromeOptions()

#cписок прокси для подключения
proxy = ['20.205.61.143:8123', '176.192.70.58:8010', '176.192.70.58	8010', '95.56.254.139:3128']
proxy = iter(proxy)

# на какой сайт заходим
url = 'https://www.eigenlayer.com/'


# читаем имеющиеся емэйлы и сохраняем в список
with open('/home/anton/env/env/BOT/1/email_registration/mails.txt', 'r') as file:
    email_adresses = list(map(str.strip ,file.readlines()))


#идем по списку емэйлов
for email in email_adresses:
    #устанавливаем для каждого запроса свой прокси по порядку из списка
    PROXY = next(proxy)
    print(PROXY)
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",
    }
    webdriver.DesiredCapabilities.CHROME['acceptSslCerts']=True

    #сам объект для соединения с драйвером браузера
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    try:
        driver.get(url=url)
        sleep(5)
        # ищем на сайте поле ввода для емэйла
        email_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter your email address']")
        email_input.clear()
        # отправляем емэил 
        email_input.send_keys(email)
        sleep(2)
        # нажимаем кнопку
        login_button = driver.find_element(By.XPATH, "//div[contains(@class,'rounded-md')]//button").click()
        sleep(2)

    except Exception as ex:
        print(ex)
        
    finally:
        driver.close()
        driver.quit()
    print('ожидаем открытия следуещего окна')
    sleep(5)    
