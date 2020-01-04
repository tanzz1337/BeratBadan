# Halo Budjank
# 1Day1Code
# MencariBeratBadanIdeal
# NoBacod
# Gaskeun..

import datetime
import sys

print("Dibuat Pada Tanggal : 10:13 Pagi,14-Juni-2019")
print("Dibuka Pada Tanggal :",datetime.datetime.now())
print()


def main():
    print("Hallo")
    print("Ini Adalah Contoh Program Sederhana\nUntuk Mencari Berat Badan Ideal Mu\n")
    print()

    a = input("Masukan Tinggi Badan Mu(cm) : ")
    if int(a) > 300:
        print("Batas Hanya Sampai 300 cm / 3 Meter")
        print("")
        return main()

    elif int(a) < 300:
        print("Setelah Kami Hitung Maka Hasilnya Seperti InI :\n")
        print("Berat Badan Normal (Max) Anda Seharusnya :",int(a) - 100,'Kg')
        print("Berat Badan Ideal Anda (Min) Seharusnya  :",(int(a) - 100 ) - (int(a) - 100) * (10 /100),'Kg')
    else:
        return main()

if __name__== main():
    run()









