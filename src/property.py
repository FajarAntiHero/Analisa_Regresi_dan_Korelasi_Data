### PROPERTI PROGRAM ANALISA REGRESI DAN KORELASI DATA ###

import os
import numpy as np

class Property:
    oneLine:str = "-"*100
    doubleLine:str = "="*100
    titleProgram:str = "program sederhana analisa regresi dan korelasi data".upper()
    programDescription:str = "Program Console ini membantu untuk menghitung serta menganalisa regresi dan korelasi koefisien \npada data user, serta dapat menampilkan diagram scatter "
    __nameData:str = None
    __nameDataX:str = None
    __nameDataY:str = None
    __databaseX:list = []
    __databaseY:list = []

    def __init__(self, nameData:str, nameDataX:str, nameDataY:str) -> None:
        Property.__nameData = nameData
        Property.__nameDataX = nameDataX
        Property.__nameDataY = nameDataY

    @classmethod
    def calc(cls, dataVariableX: list, dataVariableY: list) -> tuple[float, float, float, float, float, float, float]:
        dataX: np = np.array(dataVariableX) # Ubah List Data X menjadi Array
        dataY: np = np.array(dataVariableY) # Ubah List Data Y menjadi Array

        sigmaX: int = np.sum(dataX) # Menjumlahkan Anggota Variable X
        sigmaY: int = np.sum(dataY) # Menjumlahkan Anggota Variable Y

        dataX_power_2: np = dataX**2 # Setiap Anggota X dipanggkatkan 2
        dataY_power_2: np = dataY**2 # Setiap Anggota Y dipanggkatkan 2

        sigmaDataX_power_2: int = np.sum(dataX_power_2) # Menjumlahkan Anggota X yang telah Dipangkatkan 2
        sigmaDataY_power_2: int = np.sum(dataY_power_2) # Menjumlahkan Anggota Y yang telah Dipangkatkan 2

        sigmaX_power_2: int = sigmaX**2 # Hasil Penjuumlahan anggota variable x dipangkatkan 2
        sigmaY_power_2: int = sigmaY**2 # Hasil Penjuumlahan anggota variable Y dipangkatkan 2
        
        dataX_multiply_dataY: np = dataX * dataY # Melakukan Perkalian pada setiap anggota X dengan anggota Y
        sigma_dataX_multiply_dataY: int = np.sum(dataX_multiply_dataY) # Menjumlahkan hasil Perkalian anggota X dengan anggota anggota Y

        return sigmaX, sigmaY, sigmaDataX_power_2, sigmaDataY_power_2, sigma_dataX_multiply_dataY, sigmaX_power_2, sigmaY_power_2

    @classmethod
    def showBanner(cls) -> None:
        print(Property.doubleLine)
        print("{:^100}".format(Property.titleProgram))
        print(Property.doubleLine)
        print("{:<100}".format(Property.programDescription))
        print(Property.oneLine)

    @classmethod
    def closingBanner(cls):
        print(Property.doubleLine)
        print("{:^100}".format("Terima kasih telah menggunakan program kami!".upper()))
        print(Property.doubleLine)

    @classmethod
    def banner(cls, nameBanner:str):
        print(Property.doubleLine)
        print("{:^100}".format(str(nameBanner).upper()))
        print(Property.doubleLine)

    @classmethod
    def clearTerminal(cls) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    @classmethod
    def isNext(cls, question) -> bool:
        while True:
            isNext = input("{:<50}".format(question))

            if isNext == "Y" or isNext == "y":
                return False
            else:
                print("input jawaban tidak sesuai! ulangi!".upper())

    @property
    def getNameData(self) -> str:
        return Property.__nameData

    @property
    def getDatabaseX(self) -> list:
        return Property.__databaseX

    @property
    def getDatabaseY(self) -> list:
        return Property.__databaseY
    
    @property
    def getNameDataX(self) -> list:
        return Property.__nameDataX

    @property
    def getNameDataY(self) -> list:
        return Property.__nameDataY
    
    @getDatabaseX.setter
    def setDatabaseX(self, value:int) -> None:
        Property.__databaseX.append(int(value))

    @getDatabaseY.setter
    def setDatabaseY(self, value:int) -> None:
        Property.__databaseY.append(int(value))