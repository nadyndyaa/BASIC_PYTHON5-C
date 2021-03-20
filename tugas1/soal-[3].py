nilai_ujian_praktek = int(input("Masukkan Nilai Ujian Praktek\t:"))
nilai_ujian_teori = int(input("Masukkan Nilai Ujian teori\t:"))

if (nilai_ujian_teori >= 70) and (nilai_ujian_praktek  >= 70) :
    print("Selamat,anda lulus! ")
elif (nilai_ujian_teori >= 70) and (nilai_ujian_praktek  <= 70) :
    print("Anda harus mengulang ujian praktek.")
elif (nilai_ujian_teori <= 70) and (nilai_ujian_praktek  >= 70) :
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan ujian praktek.")