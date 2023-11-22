#ROHMAD_26_XI-TKJ2

#SOAL NO 2
#Buatlah sebuah fungsi untuk menghitung faktorial dari suatu bilangan.

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n-1)
    
bilangan_input = int(input("Masukkan bilangan untuk menghitung faktorial: "))

hasil = faktorial(bilangan_input)
print(f"Faktorial dari {bilangan_input} adalah {hasil}.")
