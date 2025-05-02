"""Soru 1: Görev Yöneticisi Uygulaması
Proje Açıklaması:
Bu ödevde, Python programlama dili kullanılarak bir görev yöneticisi uygulaması oluşturulacaktır. Bu uygulama kullanıcıların görev eklemesine, tamamlamasına, silmesine ve listelemesine olanak tanıyacaktır.

Gereksinimler:
1- Görevler bir Python listesinde saklanacak ve her görev bir sözlük (dictionary) olarak temsil edilecektir. Her görev aşağıdaki özelliklere sahip olmalıdır:

Sıra Numarası (Otomatik olarak atanmalı)

Görev Adı

Durum (Tamamlandı, Bekliyor veya Silindi)

2- Kullanıcının gerçekleştirebileceği işlemler:

Yeni bir görev ekleme

Bir görevi tamamlama

Bir görevi silme

Tamamlanan görevleri listeleme

Tüm görevleri durumlarıyla birlikte listeleme

Çıkış

3- Görevler eklendikleri sıraya göre otomatik olarak bir sıra numarası almalıdır.

4- Silinen görevlerin numaraları yerine yeni görevler eklenebilmelidir.

5- Görevler listelenirken sıra numaralarına göre sıralanmalıdır.

6- Her işlemden sonra kullanıcıya uygun bir geri bildirim verilmelidir. Örneğin, yeni bir görev eklendiğinde kullanıcıya görevin eklendiğine dair bir mesaj gösterilmelidir."""

gorevler = []

def sira_numarasi_al():
    mevcut_numaralar = {gorev["sira_numarasi"] for gorev in gorevler if gorev["durum"] != "Silindi"}
    i = 1
    while True:
        if i not in mevcut_numaralar:
            return i
        i += 1

def gorev_ekle():
    gorev_adi = input("Görev Adını Giriniz: ")
    sira_numarasi = sira_numarasi_al() 
    gorev = {"sira_numarasi": sira_numarasi, "gorev_adi": gorev_adi, "durum": "Bekliyor"}
    gorevler.append(gorev)
    print(f"Görev Eklendi: [{sira_numarasi}] {gorev_adi}")

def gorevi_tamamla():
    print(butun_gorevler_listesi())
    try:
        sira = int(input("Tamamlanacak görevin sıra numarasını girin: "))
        for gorev in gorevler:
            if gorev["sira_numarasi"] == sira and gorev["durum"] != "Silindi":
                gorev["durum"] = "Tamamlandı"
                print(f"Görev Tamamlandı: [{sira}] {gorev['gorev_adi']}")
                return
        print("Görev Bulunamadı.")  
    except ValueError:
        print("Geçersiz Giriş.")

def gorev_silme():
    try:
        sira = int(input("Silinecek görev sıra numarasını giriniz: "))
        for gorev in gorevler:
            if gorev["sira_numarasi"] == sira and gorev["durum"] != "Silindi":
                gorev["durum"] = "Silindi"
                print(f"Görev Silindi: [{sira}] {gorev['gorev_adi']}")
                return
        print("Görev bulunamadı.")  
    except ValueError:
        print("Geçersiz Giriş.")

def tamamlanan_gorev_listesi():
    print("Tamamlanan Görevler: ")
    found = False
    for gorev in sorted(gorevler, key=lambda x: x["sira_numarasi"]):
        if gorev["durum"] == "Tamamlandı":
            print(f"{gorev['sira_numarasi']} {gorev['gorev_adi']}")
            found = True
    if not found:
        print("Tamamlanan Görev Yok.")

def butun_gorevler_listesi():
    print("Bütün Görevler: ")
    found = False
    for gorev in sorted(gorevler, key=lambda x: x["sira_numarasi"]):
        if gorev["durum"] != "Silindi":
            print(f"{gorev['sira_numarasi']} {gorev['gorev_adi']} - {gorev['durum']}")
            found = True
    if not found:
        print("Listelenecek Görev Yok.")

def menu():
    print("1. Yeni görev ekle")
    print("2. Görevi tamamla")
    print("3. Görevi sil")
    print("4. Tamamlanan görevleri listele")
    print("5. Tüm görevleri listele")
    print("6. Çıkış")

def calistir():
    menu()  
    while True:
        secim = input("\nSeçiminizi yapın (1-6): ")
        
        if secim == "1":
            gorev_ekle()
        elif secim == "2":
            gorevi_tamamla()
        elif secim == "3":
            gorev_silme()
        elif secim == "4":
            tamamlanan_gorev_listesi()
        elif secim == "5":
            butun_gorevler_listesi()
        elif secim == "6":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen 1-6 arasında bir sayı girin.")
        
        menu()  

if __name__ == "__main__":
    calistir() 




