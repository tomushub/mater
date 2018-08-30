#!/usr/bin/env python
# coding: UTF-8
import sys
from ftplib import FTP
 
ftp = FTP("tgftp.nws.noaa.gov")
ftp.login()
with open("./stations/" + sys.argv[1] + ".TXT","w" ) as f:
  ftp.retrlines("RETR /data/observations/metar/stations/" + sys.argv[1] + ".TXT", f.write)
ftp.quit()
