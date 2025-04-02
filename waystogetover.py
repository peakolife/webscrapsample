#Eğer siten User-Agent filtresi koyduysa, botlar tarayıcı gibi görünmek için sahte User-Agent kullanabilir.
import requests

url = "https://asuratoon.net"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": "https://google.com",
}

response = requests.get(url, headers=headers)
print(response.text)


#Eğer site, aynı IP’den çok fazla istek atılınca engelliyorsa, botlar sürekli IP değiştirmek için proxy kullanabilir.

proxies = {
    "http": "http://12.34.56.78:8000",
    "https": "http://12.34.56.78:8000",
}

response = requests.get(url, headers=headers, proxies=proxies)
print(response.text)


#Eğer siten, içeriği JavaScript ile yüklüyorsa, botlar Selenium kullanarak tarayıcıyı taklit edebilir.
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://asuratoon.net")

print(driver.page_source)  # Tüm sayfa kaynağını al
driver.quit()


#Eğer siten, çok fazla istek atan kullanıcıya CAPTCHA gösteriyorsa, bazı botlar CAPTCHA çözücü hizmetleri (örneğin: 2Captcha, Anti-Captcha) kullanabilir.
import requests

api_key = "YOUR_2CAPTCHA_API_KEY"
captcha_response = requests.post(
    f"https://2captcha.com/in.php?key={api_key}&method=userrecaptcha&googlekey=SITE_KEY&json=1"
).json()

captcha_solution = requests.get(
    f"https://2captcha.com/res.php?key={api_key}&action=get&id={captcha_response['request']}&json=1"
).json()


#Eğer siten, botları yakalamak için görünmez tuzak linkler (honeypot) eklediyse, botlar HTML kodunu analiz ederek bu linklere tıklamaktan kaçınabilir.
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, "html.parser")
all_links = soup.find_all("a")

# Linklerde style="display: none;" olanları filtrele
valid_links = [a["href"] for a in all_links if "display: none" not in str(a)]

print(valid_links)  # Honeypot linkleri görmezden gelir


