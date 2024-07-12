import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


# Function to create a folder if it doesn't exist
def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# Selenium setup
driver_path = '/path/to/your/chromedriver'  # Update with your ChromeDriver path
options = webdriver.ChromeOptions()
options.add_argument('headless')  # Optional: Run Chrome in headless mode
driver = webdriver.Chrome(options=options)

# URL and folder setup
base_url = 'https://www.labour.gov.in/'
folder_name = 'LabourMinistryPhotoGallery'
create_folder(folder_name)

try:
    # Open the website
    driver.get(base_url)
    wait = WebDriverWait(driver, 10)
    # Click on 'Media' menu and wait for 'Photo Gallery' submenu
    media_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Media')]"))
    )
    media_menu.click()

    photo_gallery_submenu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Photo Gallery')]"))
    )
    photo_gallery_submenu.click()

    # Wait for the page to load (adjust time.sleep() as needed)
    time.sleep(3)

    # Find all image elements
    image_elements = driver.find_elements(By.XPATH, "//div[@class='photo-block']//img")

    # Extract URLs and download images
    count = 0
    for image_element in image_elements:
        if count >= 10:
            break
        image_url = image_element.get_attribute('src')
        if image_url:
            # Download the image using requests
            response = requests.get(image_url)
            if response.status_code == 200:
                # Save the image to the folder
                with open(os.path.join(folder_name, f'photo_{count + 1}.jpg'), 'wb') as f:
                    f.write(response.content)
                count += 1

    print(f"Successfully downloaded {count} photos.")

finally:
    driver.quit()