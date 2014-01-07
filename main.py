from selenium import webdriver
from SimpleCV import Camera, Display
import selenium.webdriver.support.ui as ui

cam = Camera()
img = cam.getImage()
wait = ui.WebDriverWait(driver, 10)

driver = webdriver.Firefox()
driver.get("http://images.google.com")
driver.find_element_by_xpath('//*[@id="gs_st0"]/a[1]').click()
driver.find_element_by_xpath('//*[@id="qbug"]/div/a').click()
driver.find_element_by_xpath('//*[@id="qbfile"]').click()
results = wait.until(lambda driver : driver.find_element_by_xpath('//*[@id="gbqfq"]'))
text = driver.find_element_by_xpath('//*[@id="gbqfq"]')

driver.get('http://www.eBay.in')
driver.find_element_by_xpath('//*[@id="gh-ac"]').send_keys(text)
