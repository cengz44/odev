def kalori_takip():
    ogunler = []
    
    while True:
        print("\n--- GÜNLÜK KALORİ TAKİBİ ---")
        print("1. Öğün / Yiyecek Ekle")
        print("2. Günlük Listeyi ve Toplamı Gör")
        print("3. Günlük Listeyi Sıfırla")
        print("4. Çıkış")
        
        secim = input("Seçiminiz (1-4): ").strip()
        
        if secim == "1":
            ad = input("Yiyecek/Öğün adı: ").strip()
            try:
                kalori = float(input(f"{ad} kaç kalori? (kcal): "))
                ogunler.append({"ad": ad, "kalori": kalori})
                print(f" '{ad}' ({kalori:.0f} kcal) eklendi.")
            except ValueError:
                print(" Lütfen geçerli bir sayı girin.")
                
        elif secim == "2":
            if not ogunler:
                print("\nHenüz bir öğün eklenmedi.")
            else:
                print("\n--- Bugünkü Öğünler ---")
                toplam = 0
                for idx, ogun in enumerate(ogunler, 1):
                    print(f"{idx}. {ogun['ad']}: {ogun['kalori']:.0f} kcal")
                    toplam += ogun["kalori"]
                print(f"\nToplam Tüketilen Kalori: {toplam:.0f} kcal")
                
        elif secim == "3":
            ogunler.clear()
            print(" Günlük takip sıfırlandı.")
            
        elif secim == "4":
            print("Uygulama kapatıldı.")
            break
            
        else:
            print(" Geçersiz seçim. Lütfen 1-4 arasında bir sayı girin.")

if __name__ == "__main__":
    kalori_takip()

