import datetime as dt
from datetime import date, datetime
import numpy as np


simpanan = []
pinjaman = []
bunga_simpan = 3/100
bunga_pinjam = 5/100


while True:
    print("""
    Koperasi Simpan Pinjam Kelompok 5
    Dengan NIM G.211.22.0050 Rizal Kurnia
    -----
        1. Simpanan
        2. Pinjaman
        3. Pengambilan Simpanan
        4. Pengembalian Pinjaman
        """)
    pilih = int(input("Pilih salah satu diatas: "))
    if pilih == 1:
        print("""
              1. Lihat Daftar Simpanan
              2. Tambah Daftar Simpanan
              """)
        pmenu = input("Masukkan pilihanmu: ")
        if pmenu == "1":
            print(simpanan)
        else:
            print("\nTambah Simpanan Baru\n")
            ktp = int(input("Nomor KTP: "))
            nama = input("Nama: ")
            gender = input("Jenis Kelamin: ")
            address = input("Alamat: ")
            simpan = int(input("Masukan jumlah yang ingin disimpan: "))
            waktu = dt.datetime.now().strftime("%Y-%m-%d, %H:%M")
            data = {"KTP": ktp, "Nama": nama, "jenis_kelamin": gender,
                    "Alamat": address, "jumlah_simpanan": simpan, "Tanggal": waktu}
            confirm = input("Apa anda yakin? (y/n)  ")
            if confirm == "y":
                simpanan.append(data)
    elif pilih == 2:
        print("""
              1. Lihat Daftar Pinjaman
              2. Tambah Daftar Pinjaman
              """)
        pmenu = input("Masukkan pilihanmu: ")
        if pmenu == "1":
            print(pinjaman)
        else:
            print("\nTambah Pinjaman Baru\n")
            ktp = int(input("Nomor KTP: "))
            nama = input("Nama: ")
            gender = input("Jenis Kelamin: ")
            address = input("Alamat: ")
            pinjam = int(input("Masukan jumlah yang ingin dipinjam: "))
            year = int(input('Masukkan tenggat waktu tahun: ', ))
            month = int(input('Masukkan tenggat waktu bulan: '))
            day = int(input('Masukkan tenggat waktu tanggal: '))
            data = {"KTP": ktp, "Nama": nama, "jeni_kelamin": gender, "Alamat": address, "jumlah_pinjaman": pinjam, "Tanggal": [
                year, month, day], "pembayaran_terbaru": dt.datetime.now().strftime("%d/%m/%Y")}

            confirm = input("Apa anda yakin? (y/n): ")
            if confirm == "y":
                pinjaman.append(data)

    elif pilih == 3:
        print("Pengambilan Simpanan\n")
        print(simpanan)
        index_nsbh = int(
            input(("Masuukan Index Dari Nasabah, Dimulai Dari 0: ")))
        yakin = input("Yakin? (y/n) : ")
        if yakin == "y":
            ambil = int(input("masukkan Jumlah yang ingin diambil: "))
            bef_nsbh = int(simpanan[index_nsbh]["jumlah_simpanan"]) - ambil
            print(bef_nsbh)
            simpanan[index_nsbh].update(
                {"jumlah_simpanan": bef_nsbh + bunga_simpan})
            waktu = dt.datetime.now()
            simpanan.append(waktu)
    elif pilih == 4:
        print("Pengambilan Pinjaman\n")
        print(pinjaman)
        index_nsbh = int(input(("Masuukan Index Dari Nasabah: ")))
        bayar = int(input("masukkan jumlah yang ingin dibayar:  "))
        x = pinjaman[index_nsbh]["jumlah_pinjaman"]
        nilai_akh = x + bunga_pinjam - bayar
        yakin = input("Yakin? (y/n) : ")
        if yakin == "y":
            pinjaman[index_nsbh].update({"jumlah_pinjaman": nilai_akh})
            pinjaman[index_nsbh].update(
                {"pembayaran_terbaru": dt.datetime.now().strftime("%d/%m/%Y")})
