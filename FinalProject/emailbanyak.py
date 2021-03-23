from mailmerge import MailMerge
data = read_excel('C:/Users/Nadya Wardah Budiman/Documents/IndonesiaAI/BASIC_PYTHON5-C/FinalProject/data email.xlsx').astype('str')

# email pengirim
dari = "nadya.wardah@gmail.com"

# judul atau subject
judul = "coba kirim ke banyak"

# isi password
password = "nadyacantik6"

for i in range(len(data)):
    
    kepada    = data["email"][i]
    isi_pesan = '''
Halo ''' + data["nama"][i] + ''',
Apa kabar? ini coba kirim email ke banyak orang heheheee
Semoga rapih
heheehheeheh
ok
mantappp.'''
    
    kirim_email(dari,kepada,judul,isi_pesan,password)
