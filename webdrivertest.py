import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys

def main():
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.wait = WebDriverWait(driver, 5)
        url = "https://www.google.com/search?q=who won the Superbowl"
        driver.get(url)
        sleep(5)
        try:
            ip = driver.wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "Z0LcW")
            ))
        except:
            print("Failed Bro")

        soup = BeautifulSoup(driver.page_source, "html.parser")
        answer = soup.find_all(class_="_sPg")
        if not answer:
            answer = soup.find_all(class_="Z0LcW")

        driver.quit()
        print(answer[0].get_text())


main()