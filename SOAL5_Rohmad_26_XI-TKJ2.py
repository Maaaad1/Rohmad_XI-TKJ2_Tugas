#Rohmad Wildan Salas Muchlisin_26_XI-TKJ2
#Soal 5
#Buat program Python yang mengambil nilai tugas (skala 0-100) dan nilai ujian (skala 0-100) seorang siswa dan menentukan nilai akhirnya.
#Jika nilai tugas lebih dari 70 dan nilai ujian lebih dari 60, siswa lulus dengan nilai "Lulus".
#Jika tidak, siswa gagal dengan nilai "Gagal".

#Jawaban

nilai_tugas = float(input("Masukkan nilai tugas (0-100): "))
nilai_ujian = float(input("Masukkan nilai ujian (0-100): "))

if nilai_tugas < 0 or nilai_tugas > 100 or nilai_ujian < 0 or nilai_ujian > 100:
    print("Nilai tidak sesuai")
else:
    if nilai_tugas > 70 and nilai_ujian > 60:
        hasil = "Lulus"
    else:
        hasil = "Gagal"
    
    print(f"Hasil: {hasil}")