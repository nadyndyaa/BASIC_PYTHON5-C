def manju(arah):
    if(arah == "kanan"):
        print("maju ke ==>")
    elif(arah == "kiri"):
        print("Maju ke<==")
    else:
        print("Diam")

def rintangan(jenis_rintangan):
    if (jenis_rintangan == "batu"):
        print("Lompat ke atas")
    elif(jenis_rintangan == "burung"):
        print("Merunduk kebawah")

maju("kanan")
rintangan("batu")

q = input("Mau lanjut ?")
while q != "leave":
print("Jika ada sungai dikananmu kemana kamu pergi?")
print("Tentukan langkahmu:")
print("1. Kekanan")
print("2. Kekiri")
jawab = input(" Mau lanjut?")
if(jawab == 1):
    maju("kanan")
    print("buyrrrrr")
elif(jawab == 2):
    maju("kiri"):
    print("selamat !")
q = input("Mau lanjut?")