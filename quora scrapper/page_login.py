import os, time
from selenium import webdriver

def login(email, passw, driver):
	driver.find_elements_by_xpath('//div[contains(text(), "Sign In")]')[0].click()
	time.sleep(1.8)
	driver.find_elements_by_xpath('//a[contains(text(), "I Have a Quora Account")]')[0].click()
	time.sleep(1.5)

	#tip! :: if you are using login from Quora home page use regular_login instead of normal_login
	#signing in through topic page
	login_class=driver.find_elements_by_class_name('normal_login')

	email_address=login_class[0].find_element_by_name('email')
	email_address.send_keys(email)

	password=login_class[0].find_element_by_name('password')
	password.send_keys(passw)

	time.sleep(0.5)
	login_class[0].find_elements_by_class_name('submit_button')[0].click()
	time.sleep(2)
