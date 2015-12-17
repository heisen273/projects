import os

def rename_files():
	file_list = os.listdir("/home/anton/Downloads/prank")
	directory=os.getcwd()
	print("Directory is "+directory)
	print(file_list)
	os.chdir("/home/anton/Downloads/prank")
	for file_name in file_list:
		print("Old Name - "+file_name)
		print("New Name - "+file_name.translate(None, "0123456789"))
		os.rename(file_name,file_name.translate(None, "0123456789"))

rename_files()
