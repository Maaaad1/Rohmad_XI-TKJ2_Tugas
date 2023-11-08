import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QListWidget

# Fungsi untuk menambahkan siswa ke daftar
def add_student():
    name = name_input.text()
    age = age_input.text()
    student_list.addItem(f"Nama: {name}, Umur: {age}")
    name_input.clear()
    age_input.clear()

app = QApplication(sys.argv)

# Membuat jendela utama
window = QWidget()
window.setWindowTitle("Daftar Siswa")

# Label
name_label = QLabel("Nama Siswa:")
age_label = QLabel("Umur Siswa:")

# Field masukan untuk nama siswa dan umur siswa
name_input = QLineEdit()
age_input = QLineEdit()

# Tombol untuk menambahkan siswa
add_button = QPushButton("Tambah Siswa")
add_button.clicked.connect(add_student)

# ListWidget untuk menampilkan daftar siswa
student_list = QListWidget()

# Mengatur tata letak
layout = QVBoxLayout()
layout.addWidget(name_label)
layout.addWidget(name_input)
layout.addWidget(age_label)
layout.addWidget(age_input)
layout.addWidget(add_button)
layout.addWidget(student_list)

# Mengatur tata letak utama
window.setLayout(layout)

# Menampilkan jendela
window.show()

# Menjalankan aplikasi
sys.exit(app.exec_())
