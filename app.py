from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()

chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)

driver.get('https://www.helloworld.rs/oglasi-za-posao/kategorija/programiranje/281')

elem = driver.find_element_by_xpath('//*[@id="s2id_autogen16"]')
elem.send_keys("Python")
time.sleep(2)
elem.send_keys(Keys.RETURN)


