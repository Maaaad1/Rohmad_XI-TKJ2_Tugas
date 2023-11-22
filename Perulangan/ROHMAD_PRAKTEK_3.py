#ROHMAD_26_XI-TKJ2

#SOAL NO 3
#Sebuah investasi awal sebesar 10.000 dollar tumbuh sebesar 6% setiap tahunnya.
#Buatlah program yang menghitung
#berapa tahun yang dibutuhkan agar nilai investasi melebihi 20.000 dollar.

invest_awal = 10000
target_investasi = 20000
tingkat_pertumbuhan = 0.06

tahun = 0

while invest_awal <= target_investasi:
    tahun += 1
    pertumbuhan = invest_awal * tingkat_pertumbuhan
    invest_awal += pertumbuhan

print(f"investasi akan melebihi dari {target_investasi} dollar setelah {tahun} tahun.")
