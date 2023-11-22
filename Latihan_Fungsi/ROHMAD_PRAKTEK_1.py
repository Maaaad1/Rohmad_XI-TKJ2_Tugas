#ROHMAD_26_XI-TKJ2

#SOAL NO 1
#Buatlah sebuah fungsi yang menghitung total dari deret bilangan ganjil hingga batas tertentu yang ditentukan pengguna.

def total_deret_ganjil(batas):
    total = 0
    for i in range(1, 2*batas, 2):
        total += i
    return total

batas_input = int(input("Masukkan batas deret bilangan ganjil: "))
hasil = total_deret_ganjil(batas_input)
print(f"Total deret bilangan ganjil hingga batas {batas_input} adalah {hasil}.")
