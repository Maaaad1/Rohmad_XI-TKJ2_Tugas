#Rohmad Wildan Salas Muchlisin_26_XI-TKJ2
#Soal 7
#Buat program Python yang mengambil informasi pembaruan perangkat lunak dan menentukan apakah sistem perlu di-restart.
#Jika pembaruan mengharuskan restart, program harus mencetak "Sistem perlu di-restart."
#Jika tidak, program harus mencetak "Sistem tidak perlu di-restart."

#Jawaban
def keterangan_pembaruan(pembaruan):
    if pembaruan.lower() == "yes" :
        return "Sistem perlu di-restart."
    if pembaruan.lower() == "not" :
        return "Sistem tidak perlu di-restart."
    else :
        return "Input is incorrect, Please input yes or not only"

pembaruan = input("Apakah Anda baru saja melakukan pembaruan perangkat lunak (yes/not)? ")

status_restart = keterangan_pembaruan(pembaruan)
print(status_restart)
