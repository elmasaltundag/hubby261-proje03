import tkinter as tk

# Pencere
pencere = tk.Tk()
pencere.title("Benzer Kelimeler")

# Etiket (label)
etiket = tk.Label(pencere, text="Anahtar Kelimeleri Giriniz:")
etiket.pack(padx=10, pady=10)

# Metin alanı (entry)
metinAlani = tk.Entry(pencere)
metinAlani.pack(padx=10, pady=10)

# Buton
buton = tk.Button(pencere, text="Benzer Kelimeleri Bul")
buton.pack(padx=10, pady=10)

from gensim.models import KeyedVectors

print("Model Yükleniyor...")
kelimeVektoru = KeyedVectors.load_word2vec_format('trModel100', binary=True)
print(kelimeVektoru)

# Benzer kelimeleri bulma fonksiyonu
def benzerKelimeler(event):#event olmayınca hata mesajı geldi..
    anahtarKelimeler = metinAlani.get().lower()
    listeKelimeler = anahtarKelimeler.split(",") #"," ile anahtar kelimeler ayrıştırıldı.

    for anahtarKelime in listeKelimeler:
        print("Girilen Kelime: " + str(anahtarKelime))
        oneriler = (kelimeVektoru.most_similar(positive=anahtarKelime))
        print(oneriler)

        # Önerileri rafine et
        for oneri in oneriler:
            if anahtarKelime not in oneri[0]:
                print("https://www.google.com.tr/search?q=" + oneri[0])

# Butona tıklama olayı (event) eklendi
buton.bind("<Button-1>", benzerKelimeler)

# Pencereyi görüntüle
pencere.mainloop()
