from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="full_path_where_cromedriver_is_saved")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.messenger.com/login.php?next=https%3A%2F%2Fwww.messenger.com%2Ft%2Fadmiralreborn")
driver.find_element_by_id("email").send_keys("your_email_id")
driver.find_element_by_id("pass").send_keys("your_password")
time.sleep(3)
driver.find_element_by_name("login").click()
driver.implicitly_wait(5)

driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[2]/div/ul/li[1]/div[1]/a/div/div[2]/div[1]/span").click()
time.sleep(5)
message1=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/span/div[2]/div[2]/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div")

message1.send_keys("Hello!")
message1.send_keys(Keys.ENTER)
time.sleep(3)
message11=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/span/div[2]/div[2]/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div")

message11.send_keys("Sorry..It's totally machine typed message")
message11.send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[2]/div/ul/li[2]/div[1]/a/div/div[2]/div[1]/span").click()
time.sleep(5)
message2=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/span/div[2]/div[2]/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div")

message2.send_keys("Hello!")
message2.send_keys(Keys.ENTER)
time.sleep(3)
message22=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/span/div[2]/div[2]/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div")

message22.send_keys("Sorry..It's totally machine typed message")
message22.send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()
