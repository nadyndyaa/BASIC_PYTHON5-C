import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def kirim_email(dari,kepada,judul,isi_pesan,password):

    msg = MIMEMultipart()
    msg['From'] = dari
    msg['To'] = kepada
    msg['Subject'] = judul

    msg.attach(MIMEText(isi_pesan, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(dari, password)
    text = msg.as_string()
    server.sendmail(dari, kepada, text)
    server.quit()
    
dari      = "nadya.wardah@gmail.com"       # email pengirim
kepada    = "nadya.wardah@gmail.com"       # email penerima
judul     = "coba"       # judul atau subject
isi_pesan = '''
coba
aja 
'''   # isi pesan atau body
password  = "nadyacantik6"       # isi password

# menjalankan fungsi kirim email
kirim_email(dari,kepada,judul,isi_pesan,password) 
