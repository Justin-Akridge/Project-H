import re
import requests
from bs4 import BeautifulSoup

url = "https://katapultpro.com/map/#-NURpbK4M-OBiQXdlJaS/n-NTUOCYCb49QrrrtWJ91"

response = requests.get(url).text

soup = BeautifulSoup(response, "html.parser")

pattern = re.compile(r"(\d+)\s*'\s*(\d+)\s*\"")
matches = soup.find_all(text=pattern)

for match in matches:
    feet, inches = re.findall(pattern, match)[0]
    print(f"{feet}' {inches}\"")
