def luas_lingkaran(r):
    return 3.14 * (r*r)

r = input('Masukan jari lingkaran :')
luas = luas_lingkaran(int(r))
print('Luasnya: {}'.format(luas))

def keliling_lingkaran(R):
        return 2 * 3.14 *(R)

R = input( "masukkan keliling :")
keliling = keliling_lingkaran(int(R))
print('Kelilingnya :{}'.format(keliling))

