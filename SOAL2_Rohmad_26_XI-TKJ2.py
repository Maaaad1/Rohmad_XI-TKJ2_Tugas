#Rohmad Wildan Salas Muchlisin_26_XI-TKJ2
#Soal 2
#Buat program Python yang mengambil estimasi waktu selesai proyek dan tanggal target selesai. 
#Jika estimasi waktu selesai lebih awal atau sama dengan tanggal target, program harus mencetak "Tepat waktu,"
#jika tidak, program harus mencetak "Terlambat."

#Jawaban
Target_Selesai = (input("Target Tanggal Selesai Anda (INPUT DALAM TAHUN-BULAN-TANGGAL )"))
Estimasi_Selesai = (input("Estimasi Waktu Selesai Yang Diberikan(INPUT DALAM TAHUN-BULAN-TANGGAL)"))

if Estimasi_Selesai<=Target_Selesai:
    print("Tepat Waktu")
else:
    print("Terlambat")