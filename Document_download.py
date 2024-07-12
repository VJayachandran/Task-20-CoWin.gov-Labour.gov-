
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# URL of the website
base_url = "https://labour.gov.in/"

# Send a GET request to the base URL
response = requests.get(base_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the link to the monthly progress report
    # You need to inspect the HTML of the page to find the exact location
    # Example: If the link is in an anchor tag <a> with specific text or attribute

    # Assuming the link is found in an <a> tag with specific text or attribute
    # Replace 'Monthly Progress Report' with the actual link text or attribute value
    report_link = soup.find('a', text='Monthly Progress Report')['href']

    # Join the base_url with the report_link to get the absolute URL
    full_report_url = urljoin(base_url, report_link)

    # Send a GET request to the full_report_url
    report_response = requests.get(full_report_url)

    # Check if the request for the report was successful
    if report_response.status_code == 200:
        # Get the file name from the URL
        file_name = full_report_url.split('/')[-1]

        # Save the file to local directory
        with open(file_name, 'wb') as f:
            f.write(report_response.content)

        print(f"File '{file_name}' downloaded successfully.")
    else:
        print(f"Failed to download the report. Status code: {report_response.status_code}")
else:
    print(f"Failed to retrieve data from {base_url}. Status code: {response.status_code}")