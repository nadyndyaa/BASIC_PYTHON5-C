import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def kirim_email_df(dari,kepada,judul,isi_pesan,fname,fdir,password):

    msg = MIMEMultipart()
    msg['From'] = dari
    msg['To'] = kepada
    msg['Subject'] = judul

    msg.attach(MIMEText(isi_pesan, 'plain'))
    attachment = open(fdir + fname, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % fname)
    msg.attach(part)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(dari, password)
    text = msg.as_string()
    server.sendmail(dari, kepada, text)
    server.quit()

# buat variabel parameter dari, kepada, judul, isi_pesan, fname, fdir, password

# email pengirim
dari = "xxxx@gmail.com"

# email penerima
kepada = "xxxx@gmail.com"

# judul atau subject
judul = "Coba ada file"

# isi pesan atau body
isi_pesan = '''
apakah akan masuk?
'''

# nama file, contoh file MS word "mydoc.docx"
fname     = "timeline_20191025_175132.jpg"

# file directory, contoh D:/my document/file email/
fdir = "C:/Users/Nadya Wardah Budiman/Pictures/kamis fikti/"

# isi password
password = "xxxx"

# menjalankan fungsi kirim email dengan file
kirim_email_df(dari,kepada,judul,isi_pesan,fname,fdir,password)
