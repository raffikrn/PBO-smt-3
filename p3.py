class Mahasiswa:
    nim = 0
    nama = ""

    def __init__(self, nama, nim): 
        self.nama = nama
        self.nim = nim


mhs = Mahasiswa("raffi", "14022500041")
print(mhs.nama)
print(mhs.nim)
