#ROHMAD_26_XI-TKJ2

#SOAL NO 3
#Buatlah sebuah fungsi yang menghitung nilai pangkat dari suatu bilangan dengan eksponen tertentu.

def pangkat(bilangan, eksponen):
    return bilangan ** eksponen

bilangan_input = float(input("Masukkan bilangan: "))
eksponen_input = int(input("Masukkan eksponen: "))

hasil = pangkat(bilangan_input, eksponen_input)
print(f"Hasil {bilangan_input}^{eksponen_input} adalah {hasil}.")
