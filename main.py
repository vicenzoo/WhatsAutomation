import time
from selenium.webdriver import Firefox
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = Firefox()

url = "https://web.whatsapp.com/"

browser.get(url)
wait = WebDriverWait(browser, 600)
target = '"Contato"'
string = "Mensagem"

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title.click()
inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'

msg_area = browser.find_element(By.CSS_SELECTOR, "[title='Mensagem']")

for i in range(5):    #Number of time message will be sent.
    msg_area.send_keys(string)
    msg_area.send_keys(Keys.RETURN)
