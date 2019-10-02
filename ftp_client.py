import ftplib

sesi = ftplib.FTP('10.160.10.187', 'userftp', 'userftp')
sesi.mkd('H071181002')
sesi.cwd('H071181002')
file = open('wallpaper.png', 'rb')
sesi.storbinary('STOR wallpaper.png', file)
file.close()
sesi.quit()
