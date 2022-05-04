from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


#-----------------DEFAULT CONFIG

options = Options()
options.headless = True
PATH = '/Users/adammcmurchie/2021/selenium/chromedriver'
driver = webdriver.Chrome(PATH,options=options)

#-----------------SET WEBSITE
driver.get('https://techwithtim.net')


#-----------------SET ELEMENT
search = driver.find_element_by_name('s')

#-----------------FILL IN FORM 
search.send_keys('test')
search.send_keys(Keys.RETURN)

# PRINT SOURCE
#print(driver.page_source)


try:
	# wait max 10 seconds
	main = WebDriverWait(driver,10).until(
		EC.presence_of_element_located((By.ID,'main'))
		)
except:
	print('not found')
	driver.quit()


#-----------------print
print('printing headers')
#print(main.text)


articles = main.find_elements_by_tag_name('article')
for article in articles:
	header = article.find_element_by_class_name('entry-summary')
	print(header.text)

driver.quit()