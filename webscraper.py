import re
import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://katapultpro.com/map/#-NURpbK4M-OBiQXdlJaS/n-NTUOCYCb49QrrrtWJ91"

# Send a GET request to the URL and store the response as text
response = requests.get(url).text

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response, "html.parser")

# Use regex to find all the numbers with ' and "
pattern = re.compile(r"(\d+)\s*'\s*(\d+)\s*\"")
matches = soup.find_all(text=pattern)

# Print out the matches
for match in matches:
    feet, inches = re.findall(pattern, match)[0]
    print(f"{feet}' {inches}\"")
