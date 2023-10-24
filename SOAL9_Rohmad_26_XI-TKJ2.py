#Rohmad Wildan Salas Muchlisin_26_XI-TKJ2
#Soal 9
#Buat program Python yang mengambil status persiapan proyek dan menentukan apakah proyek tersebut dapat diluncurkan.
#Jika status persiapan "Siap," program harus mencetak "Proyek diluncurkan."
#Jika status persiapan "Tunda," program harus mencetak "Proyek ditunda."

#Jawaban

status_persiapan = input("Masukkan status persiapan proyek (Siap/Tunda): ")

if status_persiapan == "Siap":
    print("Proyek diluncurkan.")
elif status_persiapan == "Tunda":
    print("Proyek ditunda.")
else:
    print("Status persiapan tidak valid. Masukkan 'Siap' atau 'Tunda'.")
