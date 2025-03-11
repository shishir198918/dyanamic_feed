
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#from webdriver_manager.core.utils import ChromeType
#
# add headless Chrome option
def Chrome_option():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--user-data-dir=/tmp/chrome-user-data")
    return options


def get_page_source(url):
    service = Service(ChromeDriverManager(chrome_type="chromium").install())
    # set up Chrome in headless mode
    driver = webdriver.Chrome(service=service,options=Chrome_option())
    driver.get(url)
    page_source=driver.page_source
    driver.quit()
    return page_source
print(get_page_source("https://www.ycombinator.com/jobs"))

