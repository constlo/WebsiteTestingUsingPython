from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#This is an End-to-end test for article loading on the blog section on Profilence's page.
#Versions: selenium 4.7.0 and Python 3.10.6.
#Usage: py loadBlogArticle.py

#Load URL https://profilence.com/category/blog/

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://profilence.com/category/blog/")

#Click on the 'READ MORE' - buttons.
readModeButton = driver.find_element(By.XPATH, "//a[@href = 'https://profilence.com/2022/11/30/back-end-developer/']")
readModeButton.click()
#If succesfull, the page URL should change to a blog URL.

assert driver.current_url == 'https://profilence.com/2022/11/30/back-end-developer/'