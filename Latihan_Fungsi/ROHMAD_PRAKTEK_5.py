#ROHMAD_26_XI-TKJ2

#SOAL NO 5
#Deskripsi Pekerjaan: Buatlah sebuah fungsi yang menghitung bilangan Fibonacci ke-n.

def fibonacci(n):
    if n <= 0:
        return "Masukkan nilai n yang lebih besar dari 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

n_input = int(input("Masukkan nilai n untuk bilangan Fibonacci: "))

hasil = fibonacci(n_input)
print(f"Bilangan Fibonacci ke-{n_input} adalah {hasil}.")
