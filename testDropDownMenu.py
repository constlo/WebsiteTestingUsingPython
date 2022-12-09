from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#This test opens chrome on fullscreen mode to access the top bar element of Profilence's website.
#Then clicks on the company drop down menu to open the "About Us" - subnav link.
#Versions: selenium 4.7.0 and Python 3.10.6.
#Web browser: Chrome

#Usage: py testDropDownMenu.py
#Returns nothing if succesfull, assertion error if not.

#load up the main page with full screen on
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://profilence.com/")
driver.maximize_window()

driver.implicitly_wait(2)

#Since we are a first-time user, the webpage will promt us to click on the "Accept cookies" - button. We click it and continue.
acceptCookiesButton = driver.find_element(By.XPATH, "//a[@id = 'hs-eu-confirmation-button']")
acceptCookiesButton.click()

#click on the company button.
dropDownButton = driver.find_element(By.XPATH, "//button[@class = 'nav-link'][@aria-expanded='false']")
dropDownButton.click()

#assert that the drop down menu has expanded. Otherwise the test cannot continue.
assert dropDownButton.get_attribute("aria-expanded")

#find the <a> element which directs us to https://profilence.com/company/.
aboutUs = driver.find_element(By.XPATH, "//a[@href = 'https://profilence.com/company/']")
aboutUs.click()
assert driver.current_url == "https://profilence.com/company/"



