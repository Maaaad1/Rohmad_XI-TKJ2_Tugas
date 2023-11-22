#ROHMAD_26_XI-TKJ2

#SOAL NO 2
#Seorang pelari ingin meningkatkan jarak tempuhnya setiap minggunya. Ia mulai dengan 5 kilometer dan meningkatkan jaraknya sebesar 10% setiap minggunya.
#Buatlah program yang menghitung
#berapa minggu yang dibutuhkan agar pelari itu dapat berlari lebih dari 10 kilometer.

jarak_lari = 5
target_jarak = 10 
tingkat_pertumbuhan = 0.1

minggu = 0

while jarak_lari <= target_jarak:
    minggu += 1
    pertumbuhan = jarak_lari * tingkat_pertumbuhan
    jarak_lari += pertumbuhan

print(f"Pelari akan berlari lebih dari {target_jarak} kilometer setelah {minggu} minggu.")
