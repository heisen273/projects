#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
import pyprind
import sys,time
print("Input must fit format /path/to/file.txt")
path=raw_input("Path to *.txt: ")
path_lst= path.split('/')
file_name= path_lst[-1]
print ''
print ''
print "Directory must fit format /path/to/folder/"
dst1=raw_input("Destination: ")
dst=dst1+file_name


def update_progress(progress):
	global text
	barLength = 2
	status = ""
	block = int(round(barLength*progress))
	if block<6:#red
		text = "\rProgress: {0} {1}% {2}".format( "\033[1;31m█\033[1;m"*block+ " "*(barLength-block), progress*10, status)
	elif block>6 and block<=12:#yellow
		text = "\rProgress: {0} {1}% {2}".format( "\033[1;33m█\033[1;m"*block+ " "*(barLength-block), progress*10, status)
	else:#green
		text = "\rProgress: {0} {1}% {2}".format( "\033[1;32m█\033[1;m"*block+ " "*(barLength-block), progress*10, status)
	sys.stdout.write(text)
	sys.stdout.flush()
    
    

def copyer(path,dst):
		start_time=time.time()
		update_progress(1)
		while os.path.exists(dst)==True:
			dst_lst=dst.split('/')
			update_progress(2)
			dst_file_name=dst_lst[-1]
			update_progress(3)
			dst=dst1+"copy "+dst_file_name
			update_progress(4)



		my_file=open(path,'r')
		update_progress(5)
		data=my_file.read()
		update_progress(6)
		my_file.close()
		update_progress(7)

		cped_file=open(dst,'w')
		update_progress(8)
		cped_file.write(data)
		update_progress(9)
		cped_file.close()
		update_progress(10)
copyer(path,dst)
print '\n'
