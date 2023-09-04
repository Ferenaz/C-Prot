def malware(dosya_yolu):#malware adında metot oluşturuldu ve parametre olara dosya_yolu verildi.
    try:
        
        with open(dosya_yolu, 'rb') as file: # Dosya binary mode ('rb') ile açıldı.
           
            file_icerik = file.read()# Dosyanın içeriği okundu.
            
            
            offset = file_icerik.find(b"MALWARE")# "MALWARE" ifadesi arandı
            
            if offset != -1: #offset değeri -1 değilse
                print("\"MALWARE\" ifadesi {} adresinde bulundu.".format(offset))#MALWARE ifadesinin hangi konumda bulunduğu yazdırıldı.
            else: #offset değeri -1 ise
                print("\"MALWARE\" ifadesi herhangi bir konumda bulunamadı.")#MALWARE ifadesinin herhangi bir konumda bulunamadığı ekrana yazdırıldı.
    except FileNotFoundError: #Dosya bulunamadığı durumda
        print("Dosya bulunamadı.") #Dosya bulunamadı olarak ekrana yazdır.
    except Exception as e:# Genel bir hata oluştuğunda
        print("Bir hata oluştu:", str(e))#Bir hata oluştu mesajını ekrana yazdır.


dosya_yolu = input("Dosya yolunu giriniz: ")# Kullanıcıdan dosya yolu alındı.

malware(dosya_yolu)# Malware'ı ara ve sonucu ekrana yazdır
input()
