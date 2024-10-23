#müşteri bilgilerini ve satın aldığı ürün bilgilerini değişkenler içerisinde sakla.
#toplam odenen ücret nedir?
#ödenen miktarın kdv oranı nedir?
musteriAd = "sadık"
musteriSoyad = "turan"
musteriTelefon = "05321234567"
musteriEmail = "info@sadikturan.com"
musteriAdres = "kocaeli"

urun1Ad = "kablosuz mouse"
urun1Fiyat = 550

urun2Ad = "kablosuz klavye"
urun2Fiyat = 650

urun3Ad = "dizustu bilgisayar"
urun3Fiyat = 55000

toplamUcret = urun1Fiyat + urun2Fiyat + urun3Fiyat
print("toplam ucret: " + str(toplamUcret))
print("toplam kdv: " + str(toplamUcret * 0.18))