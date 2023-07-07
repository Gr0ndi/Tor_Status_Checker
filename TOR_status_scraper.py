import selenium #api's are for loosers 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
options = Options()
#options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
options.add_argument('-headless')
url = "https://status.torproject.org/"
driver = webdriver.Firefox(options=options)
driver.get(url)
status = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/strong")
print(status.text)
