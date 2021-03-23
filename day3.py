 #For Loop = mengulang suatu program sebanyak yg kita inginkan
# fruits = ["apple","banana","cherry","manggis","buah naga"]
 #print(fruits[0])
 #print(fruits[1])
 #print(fruits[2])
 #print(fruits[3])


#fruits = ["apple","banana","cherry"]
 #for x in fruits:
     #print(x) 


#range
#menggunakan batasan stop saja
#for i in range(6):
    #print("i") 
#menggunakan batasan start dan stop
#for x in range(3,6):
    #print(x)
#menggunakan batasan start, stop dan step(kelipatan)
#for m in range(0,20,2):
    #print(m)

#for loop(inisialisasi ; kondisi;increment) 
#for i in range(0,6,2): # 0,1,2,3,4,5,
    #print(i)
#print("======")
#while loop (inisialisasi ; kondisi;increment) 
#i = 0 #inisialisasi
#while i  < 6:
    #print(i)
    #i += 2 #increment i = i +1 



#CONTINUE = untuk melompati suatu kondisi
#for i in range (5):
    #if i == 3:
        #continue
    #program tidak akan dicetak
   # print(i)

#for i in range (5):
    #q = input("Masukkan kode : ")
   # if q == 'm':
       # print("angka diskip")
       # continue
    #program dibawah ini tidak akan akan dieksekusi
    #ketika continue aktif
   # print(i) 

#BREAK
#for i in range(5):
   # if i == 3:
      #  break
    #print(i)


#for i in range(10):
   # q = input("Apakah anda yakin keluar ? :")
   # if q == 'y' :
       ## print("anda keluar")
       # break
  #INFINTITE LOOP
#for i in range(2):
    #print("i = {}".format(i))
    #print("Perulangan I ")
    #for j in range(3):
     #   print("j ={}".format(j))
      #  print("perulangan j")
       # print()

#satu_d = [1,2,3,4,5,6,]
#dua_d =[ [1,2,3] , [4,6,6] ]
#tiga_d = [ [ [1,2],[3,4] ] , [ [5,6],[7,8] ] ]
 #PKE NESTED LOOP
 #for i in tiga_d:
  #   for j in i:
   #      for k in j:
    #     print(k)

   # coba = [ [ "nadya","nami","key"] , [20,2,3] ]
   # for i in coba:
     #   print()
     #       for j in range(5):