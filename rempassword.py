import pikepdf
import sys
import os
import datetime
today = datetime.date.today()
threemonth = today - datetime.timedelta(days=2)
passwordlist = ["","password2","password3"]
path ="path to root folder"
filelist = []
for root, dirs, files in os.walk(path):
	for file in files:
        #append the file name to the list
		try:
			print (os.path.getctime(os.path.join(root,file)))
			if datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(root,file))).date()  > threemonth:
				filelist.append(os.path.join(root,file))
		except:
			print(" A file failed")
#print all the file names
for name in filelist:
	print(name)
	failure = 0
	if name.lower().find(".pdf") == -1 :
		continue
	tooverwrite = 0
	for passw in passwordlist:
					try:
							pdf = pikepdf.open(name)
					except:
						try:
								print (passw)
								pdf = pikepdf.open(name, password=passw,allow_overwriting_input=True)
								tooverwrite = 1
								print ("success")
								break
						except:
								failure = failure + 1
								continue

	if failure == len(passwordlist):
		print("Password not in list for" + name)
		sys.exit()
	print("\nProcessing...\n")
	if tooverwrite == 1:
		pdf.save(name.replace(".pdf",".pdf"))
		name2 = name.lower().replace("_unlocked","").replace("march","mar").replace("april","apr").replace("january","jan").replace("february","feb").replace("june","jun").replace("july","jul").replace("august","aug").replace("september","sep").replace("october","oct").replace("november","nov").replace("december","dec")
		name2 = name2.replace("statement_","")
		os.rename(name,name2)
