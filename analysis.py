import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/c/SecularTalk/videos')
driver.execute_script("window.scrollBy(0,250)", "")
driver.execute_script("window.scrollBy(0,250)", "")
driver.execute_script("window.scrollBy(0,250)", "")
driver.execute_script("window.scrollBy(0,250)", "")
driver.execute_script("window.scrollBy(0,250)", "")



WebDriverWait(driver, 20).until(lambda driver: len(driver.find_elements(By.ID, "video-title")) > int(100))


html = driver.execute_script("return document.documentElement.innerHTML")
soup = BeautifulSoup(html)


for anchor in soup.find_all(id='video-title'):
    print(anchor['href'])


