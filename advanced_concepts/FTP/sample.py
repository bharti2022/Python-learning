from ftplib import FTP
ftp = FTP('ftp.cse.buffalo.edu')
print (ftp.login())
print(ftp.retrlines('LIST'))
#'230 Guest login ok, access restrictions apply.'

# go to another dir
ftp.cwd('mirror')
print(ftp.retrlines('LIST'))

#download a file via ftp

# ftp.cwd('debian')

# out = 'README'
# with open(out, 'wb') as f:
#     ftp.retrbinary('RETR'+ 'README.html',f.write)

#upload file
# ftp = FTP()
# HOST = 'ftp.cse.buffalo.edu'
# PORT = 12345
# ftp.connect(HOST, PORT)