#!/usr/bin/env python
# coding: UTF-8
import sys
from ftplib import FTP

def read_data(airport):
	ftp = FTP("tgftp.nws.noaa.gov")
	ftp.login()
	with open("./stations/" + airport + ".TXT","w" ) as f:
		ftp.retrlines("RETR /data/observations/metar/stations/" + airport + ".TXT", f.write)
	with open("./decoded/" + airport + ".TXT","w" ) as fd:
		ftp.retrlines("RETR /data/observations/metar/decoded/" + airport + ".TXT", fd.write)
	ftp.quit()
