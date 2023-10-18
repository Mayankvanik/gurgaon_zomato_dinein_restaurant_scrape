from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

option1 = Options()
option1.add_argument("--disable-notifications")

driver = webdriver.Chrome(executable_path='C:/Users/mayan/Desktop/New folder/chromedriver.exe',chrome_options=option1)
#driver.maximize_window()
driver.get('https://www.zomato.com/ncr/dine-out-in-gurgaon')
#https://www.nobroker.in/gurgaon/buy
#height = driver.execute_script('return document.body.scrollHeight')
old_height = driver.execute_script('return document.body.scrollHeight')

while True:

    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)

    new_height = driver.execute_script('return document.body.scrollHeight')
    time.sleep(1)
    print(old_height)
    print(new_height)

    if new_height == old_height:
        break
    old_height = new_height

# time.sleep(1)
# driver.execute_script('window.scrollTo(20, document.body.scrollHeight)')

a_elements = driver.find_elements(By.TAG_NAME, "a")

# Fetch href attributes and store them
href_list = []

for a_element in a_elements:
    href = a_element.get_attribute("href")
    if href and href not in href_list:
        href_list.append(href)
        print(href)
print(len(href_list))


# with open('practice.html', 'w', encoding='utf-8') as f:
#     for href in href_list:
#         f.write(href+"\n")

html = driver.page_source

with open('img1.html','w',encoding='utf-8') as f:
      f.write(html)
# Close the WebDriver
driver.quit()

#
# with open('sector,36,37,38.html','w',encoding='utf-8') as f:
#       f.write(html)
#user_input = driver.find_element(by=By.XPATH, value='//*[@id="listPageSearchLocality"]')

