import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# configurations
username = 'username here'
password = 'password here'
project_order = [
    'P-00015-58'
    # , 'P-00026-62'
]
option_values = {
    1: ['Azure Devops eğitimi alındı'], # Alınan Eğitim
    2: ['Azure Data Lake araştırması yapıldı'], # Araştırma
    3: ['Azure servislerinin bakımı', 'OPC Servislerinin bakımı'], # Bakım
    # 4, # Danışmanlık
    5: ['ASA Geliştirme', 'OPC Client Geliştirme', 'DWH Geliştirme'], # Geliştirme
    6: ['Azure servis bugları giderme'], # Hata Giderme
    7: ['Eskişehir OPC Client kurulumu'], # Kurulum
    9: ['DWH geliştirme', 'BI Geliştirme', 'Enerji-fayda hesaplamaları'], # Raporlama
    10: ['Steerco toplantısı', 'Haftalık toplantılar', 'Kurulum toplantıları'], # Toplantı
    21: ['Eskişehir kurulumu için ön hazırlık'], # Ön Hazırlık Çalışması
}


# start a new browser session
browser = webdriver.Chrome('chromedriver.exe')

# navigate to a webpage
browser.get('http://213.153.169.56/pmtyeni/login.jsp')
login_wait = WebDriverWait(browser, 10)

# click login in button
elem = login_wait.until(EC.visibility_of_element_located((By.XPATH, ".//input[@name='userid']")))
elem.send_keys(username)
elem = login_wait.until(EC.visibility_of_element_located((By.XPATH, ".//input[@name='password']")))
elem.send_keys(password)
elem.send_keys(Keys.ENTER)
time.sleep(5)
browser.get('http://213.153.169.56/pmtyeni/servlet/com.pmt.iscilik.KisiselIscTakvimiServlet?button=no&mode=insert')

# getting only work days
elements = browser.find_elements_by_xpath("//td[@bgcolor='#8CA2F7']/table/tbody/tr/td/a")
working_days = []
for element in elements:
    working_days.append(element.get_attribute('href'))

for day in working_days:
    browser.get(day)
    time.sleep(1)
    browser.find_element_by_xpath("//input[@type='checkbox']").click()
    time.sleep(1)
    browser.find_element_by_xpath(f"//option[@value='{random.choice(project_order)}']").click()
    time.sleep(1)
    random_work = random.choice(list(option_values.keys()))
    browser.find_element_by_xpath(f"//option[@value='{str(random_work)}']").click()
    time.sleep(1)
    browser.find_element_by_xpath("//input[@name='btn0']").click()
    time.sleep(1)
    browser.find_element_by_xpath("//select[@name='efor0']/option[@value='8']").click()
    description_area = login_wait.until(EC.visibility_of_element_located((By.XPATH, ".//input[@name='aciklama0']")))
    description_area.send_keys(random.choice(option_values[random_work]))
    time.sleep(1)
    browser.find_element_by_xpath("//input[@type='SUBMIT']").click()
    time.sleep(2)

