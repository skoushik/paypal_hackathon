from selenium import webdriver
from SimpleCV import Camera, Display

cam = Camera()
disp = Display()

while disp.isNotDone():
	img = cam.getImage()
	img.show()
	if disp.mouseLeft:
		break

driver = webdriver.Firefox()
driver.get("http://images.google.com")
driver.find_element_by_xpath('//*[@id="gs_st0"]/a[1]').click
driver.find_element_by_xpath('//*[@id="qbug"]/div/a').click
driver.find_element_by_xpath('//*[@id="qbfile"]').click
text = driver.find_element_by_xpath('//*[@id="gbqfq"]')

driver.get('http://www.eBay.in')
driver.find_element_by_xpath('//*[@id="gh-ac"]').send_keys(text)

