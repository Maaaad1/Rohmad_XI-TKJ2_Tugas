#Rohmad Wildan Salas Muchlisin_26_XI-TKJ2
#Soal 6
#Buat program Python yang mengambil data penjualan bulanan produk dan menentukan kategori produk berdasarkan penjualan:
#Jika penjualan lebih dari 1000 unit, kategorikan sebagai "Produk Terlaris."
#Jika penjualan antara 500 hingga 1000 unit, kategorikan sebagai "Produk Populer."
#Jika penjualan kurang dari 500 unit, kategorikan sebagai "Produk Biasa."

#Jawaban

Nama_Barang = str(input("Masukan Nama Barang"))
Kategori = float(input("Input Jumlah Unit Yang Terjual"))

if Kategori>1000 :
    print (Nama_Barang, "Adalah Produk Terlaris")

if 500<=Kategori<1000 :
    print  (Nama_Barang, "Adalah Produk Populer")

if Kategori<500 :
    print  (Nama_Barang, "Adalah Produk Biasa")
