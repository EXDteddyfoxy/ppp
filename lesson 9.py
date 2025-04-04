import requests
from bs4 import BeautifulSoup

url = "https://www.cbar.az/currencies/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
usd_rate = float(soup.find("td", {"class": "kurs_val"}).text.strip().replace(",", "."))

amount = float(input("Введите сумму в манатах: "))
usd_amount = round(amount / usd_rate, 2)

print(f"{amount} AZN = {usd_amount} USD")