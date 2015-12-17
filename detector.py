import collections
import itertools

def detector():
	content=raw_input('Enter your message: ')
	
#	content=f.read()
	content=content.lower()
	content=content.replace(',','')
	content=content.replace('.','')
	content=content.replace('(','')
	content=content.replace(')','')	
	content=content.split()
	badwords="shit shot fuck cunt ass 13"
	badwords=badwords.split()
	
	if set(content).intersection(badwords):
:		if badwords in content:
			content.append('cleaned')		
		#content=[elements.replace(str(detected),'CLEANED') for elements in content]
		#	content.append()
			#content[content.index(str(detected))]="replace"			
		print(content)
	
	
detector()
