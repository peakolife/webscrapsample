import requests
from bs4 import BeautifulSoup

url = "https://manhuaus.com/manga/regressed-life-of-the-sword-clans-ignoble-reincarnator/chapter-1/"  # Test etmek istediğiniz sitenizin URL'si

# User-Agent sahtekarlığı yaparak bot gibi davranıyoruz
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)

# Eğer CAPTCHA, engelleme vb. durumlar varsa, burada hata kodu alabilirsiniz
if response.status_code == 200:
    print("Başarılı istekte bulunuldu!")
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.prettify())  # Sayfa kaynak kodunu yazdırır
else:
    print(f"Sayfaya erişilemedi, durum kodu: {response.status_code}")
