import ftplib
def returnDefault(ftp):
	try:
		dirList = ftp.nlst()
	except:
		dirList = []
		print '[-] Could not list directory contents.'
		print '[-] Skipping To Next Target.'
		return
	retList = []
	for fileName in dirList:
		fn = fileName.lower()
		if '.php' in fn or '.html' in fn or '.asp' in fn:
			print '[+] Found default page: ' + fileName
			retList.append(fileName)
	return retList

host = '127.0.0.1'
userName = 'anonymous'
passWord = 'user@res.com'
ftp = ftplib.FTP(host)
ftp.login(userName, passWord)
returnDefault(ftp)
