from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import selenium.common.exceptions

#This automated testing task is used to test the top bar buttons.
#This test uses selenium 4.7.0 and Python 3.10.6.
#Usage: py loadServicesPage.py

#Go to the page https://profilence.com/

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://profilence.com/")



#Since we are a first-time user, the webpage will promt us to click on the "Accept cookies" - button. We click it and continue.
acceptCookiesButton = driver.find_element(By.XPATH, "//a[@id = 'hs-eu-confirmation-button']")
acceptCookiesButton.click()
driver.implicitly_wait(2)

#The services-tab is hidden behind a button. We click this button, and continue.
menuToggleButton = driver.find_element(By.XPATH, "//button[@class = 'menu-toggle menu-toggle-main']")
menuToggleButton.click()
driver.implicitly_wait(2)

#Then, find the link element to the services page, and click it.
servicesElement = driver.find_element(By.XPATH, "//a[@class = 'nav-link'][@title = 'Services']")
servicesElement.click()

try:
    #Close the Subscribe pop up window if there is one
    closeSubWindow = driver.find_element(By.XPATH, "//button[@class = 'leadinModal-close']")
    closeSubWindow.click()
except selenium.common.exceptions.NoSuchElementException:
    #If there is no pop-up window, we continue normally.
    pass

#if the test is succesfull, the page URL should change to https://profilence.com/services/.
assert driver.current_url == "https://profilence.com/services/"