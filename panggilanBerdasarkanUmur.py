umur= int(input("masukkan umur kamu: "))
if umur <= 2:
    print("bayi")
elif umur <= 5:
    print("Balita")
elif umur <= 12:
    print("Anak-anak")
elif umur <= 17:
    print("remaja")
elif umur > 17 and umur <= 30:
    print("dewasa")
else:
    print("orang tua")

