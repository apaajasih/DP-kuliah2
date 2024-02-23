hargaMangga=0
beratMangga= 10
if beratMangga <= 2 :
    hargaMangga=20_000 * beratMangga
elif beratMangga <= 5:
    hargaMangga = 18_000 * beratMangga
elif beratMangga >= 5:
    hargaMangga = 16_000 * beratMangga

    print("harga mangga yang harus dibayar : ", hargaMangga)