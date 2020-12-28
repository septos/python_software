print("""
===========================================================
PROGRAM KASIR SEDERHANA
===========================================================
( 1 ) Baju  
( 2 ) Tas
( 3 ) Jam
""")
# x = []
# harga_barang = []
def tanya():
    while True:
            # print("=====Barang Tidak Tersedia,Silahkan Pilih  Lainnya!!=====")
            pilihan_menu = int(input("Pilih nomor barang : "))
            if pilihan_menu== 1 or pilihan_menu== 2 or pilihan_menu== 3:
                if pilihan_menu==1:
                    harga_barang = 100000
                elif pilihan_menu==2:
                    harga_barang = 90000
                elif pilihan_menu==3:
                    harga_barang = 50000

pilihan_menu = int(input("Pilih nomor barang : "))
# x = input("")
if pilihan_menu == 1:
    #harga baju 100.000
    harga_barang = 100000
elif pilihan_menu == 2:
    #harga tas 90.000
    harga_barang = 90000
    # cetak2()
elif pilihan_menu == 3:
    #harga jam 50.000
    harga_barang = 50000
else:
    tanya()
        # while True:
        #     # print("=====Barang Tidak Tersedia,Silahkan Pilih  Lainnya!!=====")
        #     pilihan_menu = int(input("Pilih nomor barang : "))
        #     if pilihan_menu== 1 or pilihan_menu== 2 or pilihan_menu== 3:
        #         if pilihan_menu==1:
        #             harga_barang = 100000
        #         elif pilihan_menu==2:
        #             harga_barang = 90000
        #         elif pilihan_menu==3:
        #             harga_barang = 50000
        #         break


print("===========================================================")
print("Harga barang = Rp",harga_barang)
print("===========================================================")
z = input("Masukan jumlah barang : ")
bayar = (int(z)*int(harga_barang))
print("===========================================================")
print("Jumlah yang harus dibayar adalah Rp",bayar)
print("===========================================================")


sleep(500)
"""





print(z)



# def inputan():




# hasil = lambda nilai:print(""harga_barang*z)

# cetak_hasil = print("Harga barang = ",harga_barang)

# inputan()
# def fungsi_inputan():
    # print(harga_barang)
# else:
#     print("xxx")

ab = []
total_harga= []


# lambda x,y:x*y

# z1 = print("Jumlah yang harus dibayar adalah: {}")


# pilihan = []
# while pilihan:
#     if pilihan == '1': 
"""
