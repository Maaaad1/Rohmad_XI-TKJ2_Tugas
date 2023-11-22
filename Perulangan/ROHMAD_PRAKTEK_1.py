#ROHMAD_26_XI-TKJ2

#SOAL NO 1
#Seorang petani memiliki 100 ekor ayam di peternakannya.
#Setiap bulan, jumlah ayam bertambah 5% dari jumlah ayam pada bulan sebelumnya.
#Buatlah program yang menghitung
#berapa bulan yang dibutuhkan agar jumlah ayam melebihi 200 ekor.

ayam_awal = 10  
target_ayam = 200  
tingkat_pertumbuhan = 0.05  

bulan = 0

while ayam_awal <= target_ayam:
    bulan += 1
    pertumbuhan = ayam_awal * tingkat_pertumbuhan
    ayam_awal += pertumbuhan
    
print(f"Jumlah ayam akan melebihi {target_ayam} ekor setelah {bulan} bulan.")
