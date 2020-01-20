import os 
import shutil
import pysftp
import logging

#declare function

def transfer_file(pathFile, logging):
	cnopts = pysftp.CnOpts()
	cnopts.hostkeys = None 
	
	#print pathFile
	logging.info("connect to server...")
	svc = pysftp.Connection(host="36.91.226.234", port=40122, username="Laprima",
	password="L4pr1MA@-", cnopts=cnopts)
	
	svc.chdir("/home/sftp/Laprima/inboxcl")
	print svc.listdir

	logging.info("transfer file : " + pathFile)
	#transfer & logging
	logging.info(svc.put(pathFile))

	data = svc.listdir()
	svc.close()


#declare variable
	
log = "/Users/otongsunandar/Workspace/RCS/Random/tes-pos-agent/svc-transferdata-tapbox.log"
inbox = "/Users/otongsunandar/Workspace/RCS/Random/tes-pos-agent/inbox"
outbox = "/Users/otongsunandar/Workspace/RCS/Random/tes-pos-agent/outbox"

#setup log

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename=log,
                    filemode='a')


#transfer file

logging.info('########### Start transfer file ###########')
logging.info('Checking.. inbox & outbox folder')

if os.path.exists(inbox) and os.path.exists(outbox):
	logging.info('Inbox & outbox folder is exist')

	files = os.listdir(inbox)
	if files == []:
		print "inbox folder is empty"
		logging.warning("Inbox folder is empty")
		logging.info('No transfer data')
	else:
		#print "List of files : "
		files.sort()
		for file in files:
			#for windows
			#src = inbox + "\\" + file
			#dst = outbox + "\\" + file
			#for linux or Mac
			src = inbox + "/" + file
			dst = outbox + "/" + file
			#transfer file
			transfer_file(src,logging)
			#move file to outbox
			shutil.move(src,dst)
else:	
	print "inbox & outbox doesn't exist"
	logging.warning("inbox & outbox doesn't exist")
    
