from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = 'https://www.sportsplits.com/races/city2surf-2024/events/1/'
path = '/Users/aaronkiss/Downloads/chromedriver-mac-arm64/chromedriver'

# Create a Service object pointing to the path of your ChromeDriver
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

# test test