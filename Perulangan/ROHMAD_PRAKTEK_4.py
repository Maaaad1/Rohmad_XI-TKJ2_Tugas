#ROHMAD_26_XI-TKJ2

#SOAL NO 4
#Seorang pedagang memiliki 100 buah apel. Setiap harinya, ia menjual 10% dari jumlah apel yang tersisa.
#Setiap bulan, jumlah ayam bertambah 5% dari jumlah ayam pada bulan sebelumnya.
#Buatlah program yang menghitung
#berapa hari yang dibutuhkan agar sisa apel kurang dari 20 buah.

jumlah_apel = 100
batas_sisa_apel = 20 
tingkat_penjualan = 0.10 

hari = 0

while jumlah_apel >= batas_sisa_apel:
    hari += 1
    penjualan = jumlah_apel * tingkat_penjualan
    jumlah_apel -= penjualan

print(f"Sisa apel akan kurang dari {batas_sisa_apel} buah setelah {hari} hari.")
