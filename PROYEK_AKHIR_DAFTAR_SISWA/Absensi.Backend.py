from tkinter import *
from openpyxl import Workbook
from openpyxl.styles import Font,Alignment,Border,Side
from tkinter import font as tkfont

root = Tk()
root.title ("Absensi Siswa")
root.resizable(width=False, height=False)
workbook = Workbook()
sheet = workbook.active

styling = tkfont.Font(family="Poppins", weight="bold", size=18)
styling2 = tkfont.Font(family="Times New Roman", size=9)

font= Font(bold=True)
border= Border (left=Side(border_style="thin", color="00000000"),
                right=Side(border_style="thin", color="00000000"),
                top=Side(border_style="thin", color="00000000"),
                bottom=Side(border_style="thin", color="00000000")
                )

alignment=Alignment(horizontal="center", vertical="center")

HEIGHT = 500
WIDTH = 600
Canvas = Canvas(root, height=HEIGHT, width=WIDTH, bg='Lightblue')
Canvas.pack()

sheet["A1"] = "Mata Pelajaran\t:"
A1 = sheet["A1"]
A1.font = font

sheet["A2"] = "Tanggal\t:"
A2 = sheet["A2"]
A2.font = font

sheet["A3"] = "NO\t:"
A3 = sheet["A3"]
A3.font = font
A3.border = border
A3.alignment = alignment

sheet["B3"] = "NAMA\t:"
B3 = sheet["B3"]
B3.font = font
B3.border = border
B3.alignment = alignment

sheet["C3"] = "NISN\t:"
C3 = sheet["C3"]
C3.font = font
C3.border = border
C3.alignment = alignment

sheet["D3"] = "KELAS\t:"
D3 = sheet["D3"]
D3.font = font
D3.border = border
D3.alignment = alignment

sheet["E3"] = "JURUSAN\t:"
E3 = sheet["E3"]
E3.font = font
E3.border = border
E3.alignment = alignment

num=0

def InsertData():
    global num
    num = num+1
    sheetnum = num + 3

    sheet["A"+str(sheetnum)] = num
    DataNo = sheet["A"+str(sheetnum)]
    DataNo.border = border
    DataNo.alignment = alignment

    sheet["B"+str(sheetnum)] = Namaentry.get()
    DataNama = sheet["B"+str(sheetnum)]
    DataNama.border = border
    DataNama.alignment = alignment

    sheet["C"+str(sheetnum)] = NISNentry.get()
    DataNISN = sheet["C"+str(sheetnum)]
    DataNISN.border = border
    DataNISN.alignment = alignment

    sheet["D"+str(sheetnum)] = Kelasentry.get()
    DataKelas = sheet["D"+str(sheetnum)]
    DataKelas.border = border
    DataKelas.alignment = alignment

    sheet["E"+str(sheetnum)] = Jurusanentry.get()
    DataJurusan = sheet["E"+str(sheetnum)]
    DataJurusan.border = border
    DataJurusan.alignment = alignment

    sheet["B1"] = mapelentry.get()
    sheet["B2"] = tanggalentry.get()

    Namaentry.delete(0, END)
    NISNentry.delete(0, END)

def SaveData():
    global Informasi
    workbook.save(filename=str(mapelentry.get())+"_"+str(tanggalentry.get())+".xlsx")
    Informasi["text"] = "Data Absen Telah Di Simpan\nNama file:" + str(mapelentry.get())+"_"+str(tanggalentry.get())+".xlsx"

def CreateNewData():
    global Informasi , num
    Informasi["text"] = "HALO👋, Masukan Data Diri Kamu Kemudian Klick Insert Ya..., Semangat🫶"
    Namaentry.delete(0, END)
    NISNentry.delete(0, END)
    Kelasentry.delete(0, END)
    Jurusanentry.delete(0, END)
    mapelentry.delete(0, END)
    tanggalentry.delete(0, END)
    num = 0



frameJudul = Frame(root, bg='white')
frameJudul.place(rely=0.025, relx=0.5, relheight=0.1, relwidth=0.8, anchor='n')
judul = Label(frameJudul, bg='white', text="Absensi Siswa", font=styling)
judul.place(relheight=1, relwidth=1)

frameMapel = Frame(root, bg='black')
frameMapel.place(rely=0.15, relx=0.5, relheight=0.06, relwidth=0.8, anchor='n')
mapelinfo = Label(frameMapel, bg='white', text="Mata Pelajaran", font=styling2)
mapelinfo.place(relwidth=0.4, relheight=1 )
mapelentry = Entry(frameMapel)
mapelentry.place(relx=0.4, relheight=1, relwidth=0.6)
mapelentry.get()

frameTanggal = Frame(root, bg='blue')
frameTanggal.place(rely=0.22, relx=0.5, relheight=0.06, relwidth=0.8, anchor='n')
tanggalinfo = Label(frameTanggal, bg='white', text="Tanggal", font=styling2)
tanggalinfo.place(relwidth=0.4, relheight=1 )
tanggalentry = Entry(frameTanggal)
tanggalentry.place(relx=0.4, relheight=1, relwidth=0.6)
tanggalentry.get()

frameNama = Frame(root, bg='blue')
frameNama.place(rely=0.29, relx=0.5, relheight=0.06, relwidth=0.8, anchor='n')
Namainfo = Label(frameNama, bg='white', text="Nama Siswa", font=styling2)
Namainfo.place(relwidth=0.4, relheight=1 )
Namaentry = Entry(frameNama)
Namaentry.place(relx=0.4, relheight=1, relwidth=0.6)
Namaentry.get()

frameNISN = Frame(root, bg='blue')
frameNISN.place(rely=0.36, relx=0.5, relheight=0.06, relwidth=0.8, anchor='n')
NISNinfo = Label(frameNISN, bg='white', text="NISN", font=styling2)
NISNinfo.place(relwidth=0.4, relheight=1 )
NISNentry = Entry(frameNISN)
NISNentry.place(relx=0.4, relheight=1, relwidth=0.6)
NISNentry.get()

frameKelas = Frame(root, bg='blue')
frameKelas.place(rely=0.43, relx=0.5, relheight=0.06, relwidth=0.8, anchor='n')
Kelasinfo = Label(frameKelas, bg='white', text="Kelas")
Kelasinfo.place(relwidth=0.4, relheight=1 )
Kelasentry = Entry(frameKelas)
Kelasentry.place(relx=0.4, relheight=1, relwidth=0.6)
Kelasentry.get()

frameJurusan = Frame(root, bg='blue')
frameJurusan.place(rely=0.50, relx=0.5, relheight=0.06, relwidth=0.8, anchor='n')
Jurusaninfo = Label(frameJurusan, bg='white', text="Jurusan", font=styling2)
Jurusaninfo.place(relwidth=0.4, relheight=1 )
Jurusanentry = Entry(frameJurusan)
Jurusanentry.place(relx=0.4, relheight=1, relwidth=0.6)
Jurusanentry.get()

Informasi = Label(root, bg='white', font=styling2, text="HALO👋, Masukan Data Diri Kamu kemudian Klick Insert Ya...., Semangat🫶")
Informasi.place(rely=0.58, relx=0.5, relheight=0.1, relwidth=0.8, anchor='n')

frameButton = Frame(root, bg='black')
frameButton.place(rely=0.69, relx=0.5, relheight=0.3, relwidth=0.3, anchor='n')
insert = Button(frameButton, text="Insert", command=InsertData)
insert.place(rely=0, relx=0.5, relheight=0.25, relwidth=1, anchor='n')
Save = Button(frameButton, text="Save", command=SaveData)
Save.place(rely=0.25, relx=0.5, relheight=0.25, relwidth=1, anchor='n')
CreateNew = Button(frameButton, text="Create New", command=CreateNewData)
CreateNew.place(rely=0.5, relx=0.5, relheight=0.25, relwidth=1, anchor='n')
Exit = Button(frameButton, text="Exit", command=root.quit)
Exit.place(rely=0.75, relx=0.5, relheight=0.25, relwidth=1, anchor='n')



root.mainloop()