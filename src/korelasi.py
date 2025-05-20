### PROGRAM MENGHITUNG KORELASI DATA ###

import numpy as np
from . import Property as pr

class Korelasi:
    __hasilKorelasiKoefisien = 0
    __hasilKorelasiDeterminasi = 0

    def __init__(self, dataVariableX: list, dataVariableY: list, dataLength: int):
        self.__dataVariableX: np = np.array(dataVariableX)
        self.__dataVariableY: np = np.array(dataVariableY)
        self.__dataLength: int = dataLength

    def startKorelasi(self) -> None:
        pr.clearTerminal()
        pr.banner("analisa korelasi koefisien data")

        # PERHITUNGAN KORELASI KOEFISIEN
        calcKorelasi = pr.calc(self.__dataVariableX, self.__dataVariableY)
        sigmaX, sigmaY, sigmaDataX_power_2, sigmaDataY_power_2, sigma_dataX_multiply_dataY, sigmaX_power_2, sigmaY_power_2 = calcKorelasi

        # Hitung Korelasi Koefisien Pearson 
        numerator = self.__dataLength * sigma_dataX_multiply_dataY - sigmaX*sigmaY
        denominator_X = self.__dataLength * sigmaDataX_power_2 - sigmaX_power_2
        denominator_Y = self.__dataLength * sigmaDataY_power_2 - sigmaY_power_2
        denominator = np.sqrt(denominator_X * denominator_Y)
        r = np.round(numerator / denominator, 4)
        r_power_2 = r**2

        Korelasi.__hasilKorelasiKoefisien = r
        Korelasi.__hasilKorelasiDeterminasi = r_power_2

        # TAMPILKAN HASIL ANALISA
        print(f"Data X : {self.__dataVariableX}")
        print(f"Data Y : {self.__dataVariableY}")
        print(f"Nilai Sigma X : {sigmaX}")
        print(f"Nilai Sigma Y : {sigmaY}")
        print(f"Nilai Sigma X*Y : {sigma_dataX_multiply_dataY}")
        print(f"Nilai Sigma X^2 : {sigmaX_power_2}")
        print(f"Nilai Sigma Y^2 : {sigmaY_power_2}")
        print(f"Nilai (Sigma X)^2  : {sigmaDataX_power_2}")
        print(f"Nilai (Sigma Y)^2  : {sigmaDataY_power_2}")
        print(pr.oneLine)
        print(f"Korelasi Koefisen Data : {r}")
        print(f"Korelasi Determinasi Data : {r_power_2}")
        print(pr.oneLine)


    @property
    def getHasilKorelasiKoefisien(self) -> int:
        return Korelasi.__hasilKorelasiKoefisien

    @property
    def getHasilKorelasiDeterminasi(self) -> int:
        return Korelasi.__hasilKorelasiDeterminasi