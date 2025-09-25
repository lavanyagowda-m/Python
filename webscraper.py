import requests
from bs4 import BeautifulSoup
url = "https://www.deccanherald.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
for i, tag in enumerate(soup.find_all(["h2", "h3"]), start=1):
    text = tag.get_text(strip=True)
    if text:
        print(f"{i}. {text}")

