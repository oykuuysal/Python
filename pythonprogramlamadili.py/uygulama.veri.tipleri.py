"""
uygulama 1: yarı çapı verilen bir dairenin alan ve cevresini hesalpa.
uygulama 2: klavyeden girilen km bilgisini mil cinsinden hesapla.
"""
#uygulama 1: 
pi = 3.14
x = float(input("yariçap: "))
sonuc = (x * x * pi)
print("alan: " + str(sonuc))
sonuc1 = (x * pi * 2)
print("cevre: " + str(sonuc1))

#uygulama 2:
mesafeKm = (input("km: "))

mesafeMil = float(mesafeKm)/1.609344
print(mesafeKm + "km= "+ str(mesafeMil)+ "mil")


