import requests
from bs4 import BeautifulSoup
from PIL import Image
import os
from io import BytesIO

# Site URL'si
url = "https://asuratoon.net/manga/spare-me-great-lord/chapter-1/"  # Örnek site

# Headers ile botu taklit etme
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Sayfayı çekme
response = requests.get(url, headers=headers)

# Başarılı yanıt alındıysa işlem yap
if response.status_code == 200:
    print("Sayfa başarıyla çekildi!")
    
    # Sayfa içeriğini BeautifulSoup ile parse etme
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Resimleri bulma
    images = soup.find_all('img')  # Sayfadaki tüm <img> etiketlerini alır
    image_urls = [img['src'] for img in images if 'src' in img.attrs]
    
    # Resimlerin indirileceği klasör
    image_folder = "downloaded_images"
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
    
    # PDF'ye dönüştürülmek üzere resimleri hazırlama
    image_list = []
    
    for idx, img_url in enumerate(image_urls):
        img_response = requests.get(img_url, headers=headers)
        
        if img_response.status_code == 200:
            # Resim dosyasını kaydetme
            img_name = os.path.join(image_folder, f"image_{idx + 1}.jpg")
            with open(img_name, 'wb') as f:
                f.write(img_response.content)
            print(f"Resim indirildi: {img_name}")
            
            # Resimi PDF formatına dönüştürmek için Pillow kullanımı
            img = Image.open(BytesIO(img_response.content))
            img = img.convert('RGB')  # PNG vb. formatlar için RGB'ye dönüştürülmeli
            image_list.append(img)
        else:
            print(f"Resim indirilemedi: {img_url}")
    
    # PDF oluşturma
    if image_list:
        pdf_path = "comic_images.pdf"
        image_list[0].save(pdf_path, save_all=True, append_images=image_list[1:], resolution=100.0, quality=95)
        print(f"PDF dosyası oluşturuldu: {pdf_path}")
else:
    print(f"Sayfaya erişilemedi, durum kodu: {response.status_code}")
