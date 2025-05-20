### PROGRAM UTAMA ANALISA REGRESI DAN KORELASI ###

from src import Property
from src import Regresi as rg
from src import Korelasi as kr

class Main(Property):

    def __init__(self, nameData, nameVariableX, nameVariableY) -> None:
        super().__init__(nameData, nameVariableX, nameVariableY)

    def main(self) -> None:
        Main.isNext("Lanjutkan Analisis Data [Y] : ")
        Main.clearTerminal()
        Main.banner("input panjang data")
        inputLengthData = int(input("{:<50}".format("Masukkan Jumlah Data yang akan dianalis : ")))

        for data in range(int(inputLengthData)):
            print(Main.oneLine)
            inputDataX = input("{:<50}".format(f"Masukkan Data X yang ke {data + 1} :"))
            inputDataY = input("{:<50}".format(f"Masukkan Data Y yang ke {data + 1} :"))
            self.setDatabaseX = inputDataX
            self.setDatabaseY = inputDataY

        print(Main.oneLine)
        Main.isNext("Lanjutkan Hitung Regresi Data [Y] : ")
        Main.clearTerminal()
        calcRegresi = rg(self.getNameData, self.getNameDataX, self.getNameDataY, self.getDatabaseX, self.getDatabaseY, inputLengthData)
        calcRegresi.startRegresi()
        Main.isNext("Lanjutkan Hitung Korelasi Koefisien Data [Y] : ")
        calcKorelasi = kr(self.getDatabaseX, self.getDatabaseY, inputLengthData)
        calcKorelasi.startKorelasi()
        Main.isNext("Tampilkan Hasil Analisa Regresi Dan Korelasi")

        Main.clearTerminal()
        Main.banner("hasil analisa regresi dan korelasi data")
        print(f"Hasil Analisa Regresi Data '{self.getNameData}' : {calcRegresi.getHasilRegresi}")
        print(f"Hasil Analisa Korelasi Koefisien Data '{self.getNameData}' : {calcKorelasi.getHasilKorelasiKoefisien}")
        print(f"Hasil Analisa Korelasi Determinasi Data '{self.getNameData}' : {calcKorelasi.getHasilKorelasiDeterminasi}")
        print(Main.oneLine)

if __name__ == "__main__":
    Main.clearTerminal()
    Main.showBanner()

    while True:
        inputJawaban = input("{:<50}".format("Apakah ingin melakukan analisa data? [Y/N] : "))

        if inputJawaban == "Y" or inputJawaban == "y":
            Main.clearTerminal()
            Main.showBanner()
            inputNamaData = input("{:<50}".format("Masukkan Nama Data Anda : "))
            inputNamaVariableX = input("{:<50}".format("Masukkan Nama Variable X Anda : "))
            inputNamaVariableY = input("{:<50}".format("Masukkan Nama Variable Y Anda : "))
            user = Main(inputNamaData, inputNamaVariableX, inputNamaVariableY)
            print(Main.oneLine)
            user.main()
            break
        elif inputJawaban == "N" or inputJawaban == "n":
            Main.clearTerminal()
            Main.closingBanner()
            break
        else:
            Main.clearTerminal()
            Main.showBanner()
            print("{:^100}".format("INPUT JAWABAN ADA TIDAK SESUAI! MOHON ULANGI"))
            print(Main.oneLine)
    
    while True:
        inputClose = input("{:<50}".format("Lanjut Akhir Program [Y] : "))
        if inputClose == "Y" or inputClose == "y":
            Main.clearTerminal()
            Main.closingBanner()
            break
        else:
            print("{:<50}".format("input program salah! mohon ulangi".upper()))
