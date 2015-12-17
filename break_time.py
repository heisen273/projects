import time
import webbrowser

num=0

print("This program has started at "+time.ctime())
while(num<3):
	time.sleep(5)
	webbrowser.open("http://google.com")
	num=num+1
print("This program has finished at"+time.ctime())
