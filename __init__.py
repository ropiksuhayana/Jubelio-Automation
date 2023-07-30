from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

def open_browser():
      
        driver.get("https://app.jubelio.com/login")
        driver.maximize_window()

def close_browser():
        driver.quit()

def scroll_down():
        # actions = ActionChains(driver)
        # actions.send_keys(Keys.PAGE_DOWN).perform()
        get_page_height_script = "return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );"
        # Loop scroll sampai habis hingga mencapai akhir halaman
        last_height = 0
        while True:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                new_height = driver.execute_script(get_page_height_script)
                if new_height == last_height:
                        break
                last_height = new_height