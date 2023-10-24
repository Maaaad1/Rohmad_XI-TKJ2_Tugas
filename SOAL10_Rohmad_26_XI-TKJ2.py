#Rohmad Wildan Salas Muchlisin_26_XI-TKJ2
#Soal 1
#Buat program Python yang mengambil durasi peminjaman buku dalam hari dan menentukan jenis pinjaman berdasarkan aturan berikut:
#Peminjaman 7 hari atau kurang: "Peminjaman Pendek"
#Peminjaman lebih dari 7 hari hingga 30 hari: "Peminjaman Menengah"
#Peminjaman lebih dari 30 hari: "Peminjaman Panjang"

#Jawaban
Kategori = float(input("Input lama meminjam anda (dalam hari 1-30) "))
if Kategori<=7 :
    print ("Peminjaman Pendek")

if 7<Kategori<=30 :
    print  ("Peminjaman Menengah")

if Kategori>30 :
    print  ("Peminjaman Panjang")
