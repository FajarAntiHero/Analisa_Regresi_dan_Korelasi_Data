### PROGRAM MENGHITUNG REGRESI DATA ###

import numpy as np
import matplotlib as mtp
mtp.use('Agg')  # Pakai backend non-GUI
import matplotlib.pyplot as plt
from . import Property as pr


class Regresi:

    __hasilRegresi = ""

    def __init__(self, nameData:str, nameVariableX:str, nameVariableY:str, dataVariableX:list, dataVariableY:list, dataLength:int) -> None:
        self.__nameVariableX = nameVariableX
        self.__nameVariableY = nameVariableY
        self.__dataVariableX = np.array(dataVariableX)
        self.__dataVariableY = np.array(dataVariableY)
        self.__dataLength = dataLength
        self.__dataName = nameData
    

    def startRegresi(self) -> None:
        pr.banner("analisa regresi pada data")
        print(f"Data Variable X = {self.__dataVariableX}")
        print(f"Data Variable Y = {self.__dataVariableY}")
        print(pr.oneLine)
        self.nameFile = input("{:<50}".format("Nama File Diagram scatter anda : "))
        print(pr.oneLine)
        pr.isNext("Lanjutkan Buat Diagram Scatter Data?")
        print(pr.oneLine)

        # TAMPILKAN GRAFIK SCATTER DATA
        plt.scatter(self.__dataVariableX, self.__dataVariableY, color='blue', label=f"Titik Pencar {self.__dataName}")
        plt.xlabel(self.__nameVariableX)
        plt.ylabel(self.__nameVariableY)
        plt.title(self.__dataName)
        plt.legend()
        plt.grid(True)
        plt.savefig(f"Diagram_Scatter/{self.nameFile}.png")
        plt.clf()

        print("{:^100}".format("regresi diagram scatter telah dibuat!".upper()))
        print("{:^100}".format(f"lihat pada file Diagram_Scatter/{self.nameFile}.png"))
        print(pr.oneLine)
        pr.isNext("Lanjut Hitung Regresi Data?")

        # PERHITUNGAN REGRESI
        calcData = pr.calc(self.__dataVariableX, self.__dataVariableY)
        sigmaX, sigmaY, sigmaDataX_power_2, sigmaDataY_power_2, sigma_dataX_multiply_dataY, sigmaX_power_2, sigmaY_power_2 = calcData
        
        # MENGHITUNG NILAI b (SLOPE / KEMIRINGAN)
        numerator_b = self.__dataLength * sigma_dataX_multiply_dataY - sigmaX * sigmaY
        denominator_b = self.__dataLength * sigmaDataX_power_2 - sigmaX_power_2
        b = np.round(numerator_b / denominator_b, 3)

        # MENGHITUNG NILAI a (INTERCEPT)
        numerator_a = sigmaY - b * sigmaX
        denominator_a = self.__dataLength
        a = np.round(numerator_a / denominator_a, 3)

        y_predict = np.round(a + b * self.__dataVariableX, 3)

        # TAMPILKAN HASIL ANALISIS REGRESI DATA
        pr.clearTerminal()
        pr.banner("Hasil Analisa regresi pada data")
        print(f"Data X : {self.__dataVariableX}")
        print(f"Data Y : {self.__dataVariableY}")
        print(f"Nilai Sigma X : {sigmaX}")
        print(f"Nilai Sigma Y : {sigmaY}")
        print(f"Nilai Sigma X*Y : {sigma_dataX_multiply_dataY}")
        print(f"Nilai Sigma X^2 : {sigmaX_power_2}")
        print(f"Nilai (Sigma X)^2  : {sigmaDataX_power_2}")
        print(f"Nilai b (Slope/Kemiringan) : {b}")
        print(f"Nilai a (Intercept) : {a}")
        print(pr.oneLine)
        print("{:<100}".format(f"Persamaan Regresi: y = {a} + {b} * X"))
        print(pr.oneLine)
        pr.isNext("Lanjut Tampilkan Diagram Scatter Dengan Garis Regresi? : ")

        # TAMPILKAN GARIS REGRESI
        pr.clearTerminal()
        pr.banner("Hasil regresi pada data")
        self.nameFile = input("{:<50}".format("Nama File Diagram scatter anda : "))
        print(pr.oneLine)

        mtp.use('Agg')  # Pakai backend non-GUI
        plt.scatter(self.__dataVariableX, self.__dataVariableY, color='blue', label=f"Titik Pencar {self.__dataName}")
        plt.plot(self.__dataVariableX, y_predict, color='red', label='Garis Regresi')
        plt.xlabel(self.__nameVariableX)
        plt.ylabel(self.__nameVariableY)
        plt.title(self.__dataName)
        plt.legend()
        plt.grid(True)
        plt.savefig(f"Regresi_Diagram_Scatter/{self.nameFile}.png")
        plt.clf()

        print("{:^100}".format("regresi diagram scatter telah dibuat!".upper()))
        print("{:^100}".format(f"lihat pada file Regresi_Diagram_Scatter/{self.nameFile}.png"))
        print(pr.oneLine)

        Regresi.__hasilRegresi = f"y = {a} + {b} * X"

    @property
    def getHasilRegresi(self) -> str:
        return Regresi.__hasilRegresi