from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.common.exceptions
#This is an End-to-end test for the Management, Developers and QA Engineers-element on the https://profilence.com/products/ - website.
#Versions: selenium 4.7.0 and Python 3.10.6.
#Usage: py testElementTabs.py

#this test runs on firefox.
#Returns nothing if true, assertion error on failed test. 

#Load URL https://profilence.com/products/
driver = webdriver.Firefox()
driver.get("https://profilence.com/products/")

#Since we are a first-time user, the webpage will promt us to click on the "Accept cookies" - button. We click it and continue.
acceptCookiesButton = driver.find_element(By.XPATH, "//a[@id = 'hs-eu-confirmation-button']")
acceptCookiesButton.click()

#The tab element works by hiding the div elements when clicking the link elements.
#When a link element is clicked, the responding div will unhide, and the other two will be hidden.
#First retrieve all of the buttons

manageMentButton = driver.find_element(By.ID, "tabby-toggle_management")
developersButton = driver.find_element(By.ID, "tabby-toggle_developers")
qaEngineersButton = driver.find_element(By.ID, "tabby-toggle_qa-engineers")

#Retrieve the divs
managementDiv = driver.find_element(By.ID, "management")
developersDiv = driver.find_element(By.ID, "developers")
qaEngineersDiv = driver.find_element(By.ID, "qa-engineers")

#click on all the buttons, and assert that all other divs are hidden.
manageMentButton.click()
assert not managementDiv.get_attribute("hidden")
assert developersDiv.get_attribute("hidden")
assert qaEngineersDiv.get_attribute("hidden")

developersButton.click()
assert managementDiv.get_attribute("hidden")
assert not developersDiv.get_attribute("hidden")
assert qaEngineersDiv.get_attribute("hidden")

qaEngineersButton.click()
assert managementDiv.get_attribute("hidden")
assert developersDiv.get_attribute("hidden")
assert not qaEngineersDiv.get_attribute("hidden")