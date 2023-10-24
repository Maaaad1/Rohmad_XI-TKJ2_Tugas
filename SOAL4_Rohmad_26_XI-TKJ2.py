#Rohmad Wildan Salas Muchlisin_26_XI-TKJ2
#Soal 4
#Buat program Python yang mengambil total belanjaan dan status anggota (biasa atau premium).Berikan diskon berdasarkan aturan berikut:
#Anggota premium: Jika total belanjaan lebih dari 500.000, berikan diskon 15%. Jika tidak, berikan diskon 10%.
#Anggota biasa: Jika total belanjaan lebih dari 300.000, berikan diskon 7%. Jika tidak, berikan diskon 0%.

#Jawaban
def hitung_diskon(total_belanjaan, status_anggota):
    if status_anggota == "1":
        if total_belanjaan > 500000:
            diskon = total_belanjaan * 0.15
        else:
            diskon = total_belanjaan * 0.10
    else:  # Untuk Anggota Non Premium
        if total_belanjaan > 300000:
            diskon = total_belanjaan * 0.07
        else:
            diskon = 0

    return diskon

total_belanjaan = float(input("Masukkan total belanjaan: "))

print("Pilih Status Anggota")
print("1. Premium")
print("2. Biasa")
status_anggota = input("Masukkan status anggota (1/2): ")

diskon = hitung_diskon(total_belanjaan, status_anggota)

if diskon > 0:
    print(f"Diskon yang diberikan: Rp {diskon:.2f}")
else:
    print("Maaf, tidak ada diskon yang diberikan.")

Total_Bayar = float(total_belanjaan-diskon)
print("Total Bayar Anda Adalah", Total_Bayar )