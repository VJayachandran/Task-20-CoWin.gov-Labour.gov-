from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

# Replace with the path to your chromedriver
driver_path = '/path/to/chromedriver'

# Initialize Chrome WebDriver
service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')  # Maximize the browser window on start
driver = webdriver.Chrome(service=service, options=options)
driver = webdriver.Chrome(executable_path = driver_path, options=options)

# Open the main URL
driver.get('https://www.cowin.gov.in/')

# Wait for the page to load
wait = WebDriverWait(driver, 10)

# Find and click on the FAQ link
faq_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'FAQ')))
faq_link.click()

# Find and click on the Partners link
partners_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Partners')))
partners_link.click()

# Handle the new windows or tabs
main_window = driver.current_window_handle
all_handles = driver.window_handles

# Dictionary to store window handles and their titles
window_info = {}

# Iterate through all handles and switch to the new ones
for handle in all_handles:
    if handle != main_window:
        driver.switch_to.window(handle)
        window_info[handle] = driver.title
        print(f"Window ID: {handle}, Title: {driver.title}")
        driver.close()  # Close the new window/tab

# Switch back to the main window
driver.switch_to.window(main_window)

# Display information about the main window
print(f"Back to main window: Title - {driver.title}, URL - {driver.current_url}")

# Close the main browser window
driver.quit()