#ROHMAD_26_XI-TKJ2

#SOAL NO 4
#Deskripsi Pekerjaan: Buatlah sebuah fungsi untuk menghitung jumlah digit dari suatu bilangan.

def jumlah_digit(bilangan):
    return sum(int(digit) for digit in str(abs(bilangan)))

bilangan_input = int(input("Masukkan bilangan: "))

hasil = jumlah_digit(bilangan_input)
print(f"Jumlah digit dari {bilangan_input} adalah {hasil}.")

