from ftplib import FTP

ftp = FTP("tgftp.nws.noaa.gov")
ftp.login()
with open("./decoded/" + "RJTT" + ".TXT","w" ) as fd:
	ftp.retrlines("RETR /data/observations/metar/decoded/" + "RJTT" + ".TXT", fd.write)
ftp.quit()
