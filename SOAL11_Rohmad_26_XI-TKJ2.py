#Rohmad Wildan Salas Muchlisin_26_XI-TKJ2
#Soal 1
#Buat program Python yang mengambil nilai performa karyawan (1 hingga 5, dengan 5 sebagai performa terbaik) dan menghitung bonus tahunan berdasarkan aturan berikut:
#Jika estimasi waktu selesai lebih awal atau sama dengan tanggal target, program harus mencetak "Tepat waktu,"
#Performa 5: Bonus 20% dari gaji tahunan.
#Performa 4: Bonus 10% dari gaji tahunan.
#Performa 3: Bonus 5% dari gaji tahunan.
#Performa 2: Bonus 2% dari gaji tahunan.
#Performa 1: Tidak ada bonus.

#Jawaban
performa = int(input("Masukkan nilai performa karyawan (1-5): "))
gaji_tahunan = float(input("Masukkan gaji tahunan karyawan: "))

if performa == 5:
    bonus = 0.20 * gaji_tahunan
elif performa == 4:
    bonus = 0.10 * gaji_tahunan
elif performa == 3:
    bonus = 0.05 * gaji_tahunan
elif performa == 2:
    bonus = 0.02 * gaji_tahunan
elif performa == 1:
    bonus = 0.00
else:
    print("Nilai performa tidak valid. Masukkan nilai antara 1 hingga 5.")
    bonus = 0.00

if bonus > 0:
    print(f"Bonus tahunan karyawan: Rp{bonus:.2f}")
else:
    print("Tidak ada bonus tahunan.")

Gaji_Diterima = gaji_tahunan + bonus
print(f"Total Gaji Yang Diterima: Rp{Gaji_Diterima}")
