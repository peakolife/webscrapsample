import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os
import time  # time kütüphanesini dahil et

# Web sayfasının URL'sini girin
url = 'https://manhuaus.com/manga/regressed-life-of-the-sword-clans-ignoble-reincarnator/chapter-1/'

# HTTP isteği yapmak için headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# WebDriver'ı başlatıyoruz
driver = webdriver.Chrome(executable_path='E:\coding\learningjs\scraping-bot\chromedriver')
driver.get('https://manhuaus.com/manga/regressed-life-of-the-sword-clans-ignoble-reincarnator/chapter-1/')

# Sayfa tamamen yüklenene kadar bekliyoruz
time.sleep(5)  # Sayfa yüklenmesi için 5 saniye bekle

# Sayfa içeriğini alıyoruz
page_content = driver.page_source

# BeautifulSoup ile sayfa içeriğini işliyoruz
from bs4 import BeautifulSoup
soup = BeautifulSoup(page_content, 'html.parser')

# Buradan sonra image ve başlıkları çekebilirsiniz





# Sayfayı indir
response = requests.get(url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Resimleri bulma (Örnek olarak, <img> etiketini kullanıyoruz)
    image_tags = soup.find_all('img')

    # Resimleri kaydetmek için bir klasör oluşturun
    folder = 'downloaded_images'
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Her bir resim URL'sini indir
    for i, img in enumerate(image_tags):
        img_url = img.get('src')
        if img_url:
            # Tam URL'yi kontrol et (bağlantılar relative olabiliyor)
            if not img_url.startswith('http'):
                img_url = 'https://manhuaus.com/manga/regressed-life-of-the-sword-clans-ignoble-reincarnator/chapter-1/' + img_url
        
            # Resmi indir
            img_data = requests.get(img_url).content
            img_name = f"{folder}/image_{i + 1}.jpg"
        
            # Resmi kaydet
            with open(img_name, 'wb') as f:
                f.write(img_data)
        
            print(f"İndirilen: {img_name}")
        
            # Her resim indirildikten sonra 2 saniye bekleyin
            time.sleep(2)  # Burada bekleme süresi belirliyoruz
else:
    print(f"Hata: {response.status_code}")


