gorevler = []

def sira_numarasi_al():
    mevcut_numaralar = {gorev['sira_numarasi'] for gorev in gorevler if gorev['durum'] != "Silindi"}
    i = 1
    while True:
        if i not in mevcut_numaralar:
            return i
        i += 1

def yeni_gorev_ekle():
    gorev_adi = input("Yeni Görev Adını Giriniz: ")
    sira_numarasi = sira_numarasi_al()
    gorev = {"sira_numarasi": sira_numarasi, "gorev_adi": gorev_adi, "durum": "Bekleniyor"}
    gorevler.append(gorev)
    print(f"Görev Eklendi: {sira_numarasi} - {gorev_adi}")

def butun_listeyi_goruntule():
    print("Bütün Görevler: ")
    found = False
    for gorev in sorted(gorevler, key=lambda x: x["sira_numarasi"]):
        if gorev["durum"] != "Silindi":
            print(f"{gorev['sira_numarasi']} - {gorev['gorev_adi']} - {gorev['durum']}")
            found = True
    if not found:
        print("Listelenecek Görev Yok.")

def tamamlanan_gorevleri_listele():
    print("Tamamlanan Görevler:")
    found = False
    for gorev in sorted(gorevler, key=lambda x: x["sira_numarasi"]):
        if gorev["durum"] == "Tamamlandı":
            print(f"{gorev['sira_numarasi']} - {gorev['gorev_adi']}")
            found = True
    if not found:
        print("Tamamlanan Görev Yok.")

def gorevi_tamamla():
    aktif_gorevler = [g for g in gorevler if g["durum"] != "Silindi"]
    if not aktif_gorevler:
        print("Tamamlanacak görev yok.")
        return
    print("Seçim Yapabilmeniz İçin Bütün Liste Getiriliyor.")
    butun_listeyi_goruntule()
    try:
        sira = int(input("Tamamlanacak Görevin Sıra Numarasını Giriniz: "))
        for gorev in gorevler:
            if gorev["sira_numarasi"] == sira and gorev["durum"] != "Silindi":
                gorev["durum"] = "Tamamlandı"
                print(f"Görev Tamamlandı: {gorev['sira_numarasi']} - {gorev['gorev_adi']}")
                return
        print("Görev Bulunamadı.")
    except ValueError:
        print("Geçersiz Giriş Yaptınız.")

def gorevi_sil():
    aktif_gorevler = [g for g in gorevler if g["durum"] != "Silindi"]
    if not aktif_gorevler:
        print("Silinecek görev yok.")
        return
    print("Seçim Yapabilmeniz İçin Bütün Liste Getiriliyor.")
    butun_listeyi_goruntule()
    try:
        sira = int(input("Silenecek Görevin Sıra Numarasını Giriniz: "))
        for gorev in gorevler:
            if gorev["sira_numarasi"] == sira and gorev["durum"] != "Silindi":
                gorev["durum"] = "Silindi"
                print(f"Görev Silindi: {gorev['sira_numarasi']} - {gorev['gorev_adi']}")
                return
        print("Görev bulunamadı.") 
    except ValueError:
        print("Geçersiz Giriş Yaptınız.")

def menu():
    print("")
    print("1. Yeni Görev Ekle")
    print("2. Bütün Listeyi Görüntüle")
    print("3. Tamamlanan GÖrevleri Listele")
    print("4. Görevi Tamamla")
    print("5. Görevi Sil")
    print("6. Çıkış")

def calistir():
    menu()
    
    while True:
        secim = input("\n1-6 Arasında Seçim Yapınız:\n...")
        if secim == "1":
            yeni_gorev_ekle()
        elif secim == "2":
            butun_listeyi_goruntule()
        elif secim == "3":
            tamamlanan_gorevleri_listele()
        elif secim == "4":
            gorevi_tamamla()
        elif secim == "5":
            gorevi_sil()
        elif secim == "6":
            print("Çıkış Yapılıyor...")
            break
        else:
            print("Geçersiz Seçim.")

        menu()

if __name__=="__main__":
    calistir()
#push larama öğrenme



