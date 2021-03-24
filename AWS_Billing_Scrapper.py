# Requirments
# - pip install selenium
# - pip install webdriver_manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

aws_accountid = "" #Add AWS Account ID
aws_username = "" #Add IAM Username
aws_password = "" #Add IAM Password


if __name__ == '__main__':

    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')

    browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
    URL = "https://console.aws.amazon.com/billing/home?#/bills?year=2021&month=1"
    browser.get(URL)
    time.sleep(5) # Let the user actually see something!
    find_iam_user_radio_button = browser.find_element_by_id("iam_user_radio_button")
    find_iam_user_radio_button.click()
    time.sleep(1)
    find_resolving_input = browser.find_element_by_id("resolving_input")
    find_resolving_input.send_keys(aws_accountid)
    time.sleep(3)
    find_next_button = browser.find_element_by_id("next_button")
    find_next_button.click()
    time.sleep(3)
    find_username = browser.find_element_by_id("username")
    find_password = browser.find_element_by_id("password")
    find_username.send_keys(aws_username)
    time.sleep(1)
    find_password.send_keys(aws_password)
    time.sleep(3)
    find_signin_button = browser.find_element_by_id("signin_button")
    find_signin_button.click()
    time.sleep(10)
    browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div/div/div/div[2]/div/div/div/div/div/div/div/div[5]/div/div/div/div/div/div/div[2]/div/awsui-expandable-section/h3').click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div/div/div/div[2]/div/div/div/div/div/div/div/div[5]/div/div/div/div/div/div/div[2]/div/awsui-expandable-section/div/span/div/div/div[1]/button').click()

