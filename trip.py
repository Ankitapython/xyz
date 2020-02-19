import time

from selenium import webdriver

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://www.tripadvisor.in/")
driver.find_element_by_xpath("//span[text()='Search']").click()
driver.find_element_by_id("mainSearch").send_keys("Club Mahindra")
driver.find_element_by_xpath("//div[text()='Search']").click()
driver.find_element_by_xpath("//span[text()='Club Mahindra Varca Beach']").click()
window = driver.window_handles[1]
driver.switch_to.window(window)
time.sleep(2)

driver.find_element_by_xpath("//a[text()='Write a review']").click()
window_1 = driver.window_handles[2]
driver.switch_to.window(window_1)
mov=driver.find_element_by_xpath("//span[@id='bubble_rating']")
a=ActionChains(driver)
a.move_to_element(mov).perform()

driver.find_element_by_id("ReviewTitle").send_keys("Good  Experience")
driver.find_element_by_xpath("//textarea[@name='ReviewText']").send_keys("Tripadvisor wishes to ensure that reviewers are not affiliated in any way with the establishment they are reviewing. By checking this box, you certify that you are not employed by the establishment, are not related to anyone employed there, and do not otherwise have a business or personal relationship with the owners or managers of this establishment or a competitor that might bias your review. In addition to being a violation of our terms of service and an unethical practice, committing fraud on reviews is also")

driver.find_element_by_xpath("//div[text()='Business']").click()
driver.find_element_by_xpath("//input[@type='checkbox']").click()
driver.find_element_by_xpath("//div[@id='SUBMIT']").click()