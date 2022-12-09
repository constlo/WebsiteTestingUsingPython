from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import selenium.common.exceptions
import sys
import time

#This test is used to click through the swiper element in profilence website, with user-specified click interval.
#Uses selenium 4.7.0 and Python 3.10.6
#Usage: py testSwiperElement timeInterval
#Time interval must be greater or equal to zero

argc = len(sys.argv)
if(argc > 2):
    print(f"Error: expected one argument, got {argc - 1}")
    raise SystemExit(2)
elif argc < 1:
    print(f"Error: No arguments provided.\nUsage: py testSwiperElement.py timeInterval, where timeInterval > 0")
    raise SystemExit(2)
timeInterval = float(sys.argv[1])
if timeInterval <= 0:
    print(f"Error: timeInterval {timeInterval} must be above zero.")
    raise SystemExit(1)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://profilence.com/")

#Since we are a first-time user, the webpage will promt us to click on the "Accept cookies" - button. We click it and continue.
acceptCookiesButton = driver.find_element(By.XPATH, "//a[@id = 'hs-eu-confirmation-button']")
acceptCookiesButton.click()

clicks = 5

buttons = []
#Retrieve the buttons. Their unique attribute is "aria-label x", where x is the slide number.
#We then insert these elements into the list defined above.
buttons.append(driver.find_element(By.XPATH, "//span[@aria-label = 'Go to slide 1']"))
buttons.append(driver.find_element(By.XPATH, "//span[@aria-label = 'Go to slide 2']"))
buttons.append(driver.find_element(By.XPATH, "//span[@aria-label = 'Go to slide 3']"))
buttons.append(driver.find_element(By.XPATH, "//span[@aria-label = 'Go to slide 4']"))
buttons.append(driver.find_element(By.XPATH, "//span[@aria-label = 'Go to slide 5']"))

#We use time.sleep() here to test the click times, since the user won't wait for the animations to finish
for i in range(clicks):
    #This test can take long. During page load, at around 20 seconds, a subscription box will appear.
    try:
        #Close the Subscribe pop up window if there is one
        closeSubWindow = driver.find_element(By.XPATH, "//button[@class = 'leadinModal-close']")
        closeSubWindow.click()
    except selenium.common.exceptions.NoSuchElementException:
        #If there is no pop-up window, we continue normally.
        pass

    buttons[i].click()
    #we check that whatever button we clicked, its attribute changes from swiper-pagination-bullet to swiper-pagination-bullet-active
    #Raise an error if not
    assert buttons[i].get_attribute("class") == "swiper-pagination-bullet swiper-pagination-bullet-active"
    time.sleep(timeInterval)

