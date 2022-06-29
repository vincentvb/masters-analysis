from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
import time

driver = webdriver.Chrome()
driver.get('https://web.archive.org/web/20190615000000*/https://socialblade.com/youtube/user/jesuslostchildren777')

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'sparkline-year-label'))
)

buttons = driver.find_elements_by_class_name("sparkline-year-label")
element = None
for x in range(len(buttons)):
    if buttons[x].text == "2019":
        element = buttons[x]

element.click()

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'calendar-day '))
).click()

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'snapshot-link'))
).click()

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, 'AverageViewsPerMonth'))
)

men_menu = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Jan 18']")))

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, 'AverageViewsPerMonth')).click().perform()


