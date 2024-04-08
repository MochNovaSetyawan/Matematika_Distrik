# Buatlah program logika python pada jupyter notebook anda
# konversi nilai ke huruf mahasiswa dengan ketentuan sbb:
#A --> 85 - 100
#B --> 75 - 84
#C --> 64 - 74
#D --> 54 - 63
#E < 54


class kategori_nilai:
    def __init__(self, Nilai):
        self.Nilai = Nilai

    def function(self):
        if 85 <= self.Nilai <= 100:
            return "A"
        elif 75 <= self.Nilai <= 84:
            return "B"
        elif 64 <= self.Nilai <= 74:
            return "C"
        elif 54 <= self.Nilai <= 63:
            return "D"
        elif self.Nilai < 54:
            return "E"
        else:
            return "Nilai di luar rentang yang ditentukan"

    def Tampilan_Info(self):
        print(f"Nilai yang didapat adalah: {self.function()}")

    def Tampilan_Input(self):
        self.Nilai = int(input("Berapa nilai Anda: "))


nilai_mahasiswa = kategori_nilai(0)
nilai_mahasiswa.Tampilan_Input()
nilai_mahasiswa.Tampilan_Info()