
nilaiInggris= int(input("Masukkan nilai Inggris: "))
nilaiMTK= int(input("Masukkan nilai MTK: "))
nilaiIndo= int(input("Masukkan nilai Indoensia: "))
nilaiIPA= int(input("Masukkan nilai IPA: "))
nilaiIPS= int(input("Masukkan nilai IPS: "))

nilaiRatarata=(nilaiIPS+nilaiIPA+nilaiInggris+nilaiMTK+nilaiIndo)/2

if (nilaiIndo+nilaiMTK+nilaiInggris)/2 >= 75:
    print("kamu lulus 1")
elif nilaiRatarata >=70:
    print("kamu lulus 2")
elif nilaiInggris > 90 and nilaiMTK > 90:
    print("kamu lulus 3")
else:
    print("coba lagi")