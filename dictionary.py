#make array
thisdict ={   #dictionary
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 1964
}
thislist = ["Ford","Mustang",1964] #list
#display all
print(thisdict)         #dictonary
print(thislist)         #list

#change value
thisdict["year"] = 2018
thislist[2] = 2020

#accessing items
print(thisdict["year"])
print(thislist[2])

#display all
print(thisdict)
print(thislist)


#loop display dictionary
for x in thisdict:
    print(x)

#tambah key baru
thisdict["harga"] = 280000
print(thisdict)

#mamafaatkan list untuk membuat datadictionary yg banyak