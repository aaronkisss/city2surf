from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

website = 'https://www.sportsplits.com/races/city2surf-2024/events/1/'
path = '/Users/aaronkiss/Downloads/chromedriver-mac-arm64/chromedriver'

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

race_data = []
page_count = 0  # Initialize page counter

# Start processing pages
while page_count < 10:
    # Wait for the table to be visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'table tbody')))
    rows = driver.find_elements(By.CSS_SELECTOR, 'table tbody tr')

    for row in rows:
        position = row.find_element(By.CSS_SELECTOR, 'td:nth-child(1)').text
        name = row.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text
        race_time = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text
        race_data.append((position, name, race_time))

    # Try to find and click the "Next" button
    next_button = driver.find_element(By.CSS_SELECTOR, 'a.page-link[rel="next"]')
    if "disabled" in next_button.get_attribute("class"):
        break  # If 'disabled' is part of the class attribute, stop looping
    else:
        next_button.click()
        WebDriverWait(driver, 10).until(EC.staleness_of(rows[0]))  # Wait for the first row to be stale before reloading
        page_count += 1  # Increment page counter after successfully loading a new page

# Close the browser after processing all entries
driver.quit()

# Print all collected data
for data in race_data:
    print(f"{data[0]}, {data[1]}, {data[2]}")






