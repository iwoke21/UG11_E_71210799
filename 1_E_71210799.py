#{fungsi pangkat akar}

print("Menu Program Yang Tersedia")
print("1. pangkatkan angka")
print("2. akarkan bilangan")
pilihan = int(input("Masukkan pilihan yang diinginkan : "))


def pangkatAngka():
    print("Masukkan angka yang ingin di pangkatkan : ")
    angka1 = float(input("Angka : "))
    print("ingin memodifikasi pangkat ? (yes/no)")
    yesno = input(": ")
    if yesno == "yes":
        angka2 = int(input("Masukkan nilai pangkat : "))
        hasil1 = angka1 ** angka2
        print("Hasil dari",angka1,"^",angka2," = ",hasil1)


    else :
        hasil2 = angka1 ** 2
        print("Hasil dari",angka1,"^2"," = ",hasil2)


def akarBilangan():
    print("Masukkan angka yang ingin di akar")
    angka1 = float(input("Angka : "))
    print("ingin memodifikasi akar ? (yes/no)")


    yesno = input(": ")
    if yesno == "yes":
        angka2 = float(input("Masukkan nilai akar : "))
        hasil1 = angka1 ** (1/angka2)
        print("Hasil akar pangkat ", angka2, " dari ", angka1, " = ",hasil1)
    else :
        hasil2 = angka1 ** (1/2)
        print("Hasil akar pangkat 2 dari",angka1," = ",'{0:.2f}'.format(hasil2))


if pilihan == 1:
    pangkatAngka()


else :
    akarBilangan()