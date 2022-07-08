from selenium import webdriver

browser = webdriver.Firefox()

url = "https://google.com"

browser.get(url)

find = browser.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
find.click()
