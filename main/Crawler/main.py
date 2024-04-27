from bs4 import BeautifulSoup
import requests


response = requests.get("https://www.bing.com/search?pglt=513&q=bs4&cvid=c3bb48cea8444beba5d2d5e5ac0b20a3&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQABhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQABhAMgYICBAAGEDSAQkxNTM3M2owajGoAgiwAgE&FORM=ANNTA1&PC=U531&mkt=zh-CN")
print(response.text)