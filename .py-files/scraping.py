
import requests

# Send a GET request to the webpage
response = requests.get("https://example.com")

# Print the status code of the response
print(response.status_code)

from bs4 import BeautifulSoup

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Display the structured format of the parsed content
print(soup.prettify())


# Extract and print the page title
title = soup.title.string
print("Page Title:", title)



# Find all hyperlinks on the page
links = soup.find_all('a')

# Loop through each link and print the hyperlink reference
for link in links:
    print(link.get('href'))










