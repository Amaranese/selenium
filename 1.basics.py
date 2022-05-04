from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#-----------------DEFAULT CONFIG
options = Options()
options.headless = True
PATH = '/Users/adammcmurchie/2021/selenium/chromedriver'
driver = webdriver.Chrome(PATH,options=options)

#-----------------SET WEBSITE
driver.get('https://techwithtim.net')


#-----------------PRINT TITLE
print(driver.title)

driver.quit()