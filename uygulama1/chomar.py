try:
    
    dosya_yolu = input("Dosya yolunu girin: ")# Dosya yolu kullanıcıdan alındı.

    
    with open(dosya_yolu, 'rb') as file:# Dosyayı aç 
        ilk_iki_bayt = file.read(2)#Dosyanın içeriğinden ilk iki baytı oku.

        
        if len(ilk_iki_bayt) == 2: # Okunan baytları ekrana yazdır
            print("Dosyanın ilk iki baytı:", ilk_iki_bayt.decode('utf-8'))
        else:#Aksi durumda
            print("Dosyanın ilk iki baytı okunamadı.")#Dosyanın ilk iki baytı okunamadı şeklinde ekrana yazdır.

except FileNotFoundError:#Dosyanın bulunamadığı hata durumunda
    print("Dosya bulunamadı.")#Dosya bulunamadı mesajını ekrana yazdır.
except Exception as e:#Dosya ile ilgili genel br hata oluştuğunda
    print("Bir hata oluştu:", str(e))#Bir hata oluştu mesajını ekrana yazdır.
input()
