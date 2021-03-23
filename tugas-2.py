def daftarkontak():
    print("\nDaftar Kontak:")
    print("Nama: Nafi")
    print("No Telepon: 08123456789")
    print("Nama: Joko")
    print("No Telepon:08987654321")

def tambahkontak():
    name  = input("\nNama \t\t:")
    no = input("No Telepon \t:")
    print("\nKontak berhasil ditambahkan")

def exit():
    print("Program selesai sampai jumpa!")
    
print('\nSelamat Datang!') 
print('\n---Menu---')
print('1. Daftar Kontak')
print('2. Tambah Kontak')
print('3. Keluar')
print('========================')

while True:
    pilih = input('\nPilihan menu :')

    if pilih == "1" :
         daftarkontak()
    elif pilih == "2" :
        tambahkontak()
    elif pilih == "3" :
        exit()   
        break
    else:
        print("Menu tidak tersedia")
    