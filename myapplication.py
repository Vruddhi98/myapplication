import os
import pyttsx3

pyttsx3.speak("Welcome to my tools")
print ("=======================Welcome to my tools !=========================")

pyttsx3.speak("How can I help you ?")
print("How can I help you ?")

while True :
	pyttsx3.speak("Tell me your requirements")
	print("Tell me your requirements : ", end =' ')
	a = input()

	
	
	if ( ("run" in a ) or ("launch" in a) or ("execute" in a) or ("open" in a) or ("start" in a)) and ( ("notepad" in a) or ("text editor" in a) or ("text" in a) ) :
		pyttsx3.speak("Opening notepad")		
		os.system("notepad")
		print("Notepad successfully opened")
	elif (("run" in a ) or ("launch" in a) or ("execute" in a) or ("open" in a)or ("start" in a)) and (("chrome" in a) or ("google chrome" in a)) :
		pyttsx3.speak("Opening google chrome")
		os.system("chrome")
		print("Google chrome successfully opened")
	elif (("run" in a ) or ("launch" in a) or ("execute" in a) or ("open" in a)or ("start" in a)) and (("sublime" in a) or ("sublime_text" in a) or ("sublime text 3" in a)) :
		pyttsx3.speak("Opening sublime ")
		os.system("sublime_text")
		print("Sublime successfully opened")
	elif (("run" in a ) or ("launch" in a) or ("execute" in a) or ("open" in a)or ("start" in a)) and (("explore" in a) or ("internet explorer" in a) or("ie" in a)) :
		pyttsx3.speak("Opening internet explorer")
		os.system("iexplore")
		print("Internet explorer successfully opened")
	elif (("run" in a ) or ("launch" in a) or ("execute" in a) or ("start" in a) or ("open" in a)) and (("zoom" in a) or ("zoom launcher" in a) or ("meeting" in a))  :
		pyttsx3.speak("Opening zoom")
		os.system("zoom")
		print("Zoom successfully opened")
	elif (("run" in a ) or ("launch" in a) or ("execute" in a) or ("open" in a) or ("start" in a)) and (("wmplayer" in a) or ("windows media player" in a) or ("wmp" in a)  or ("media player" in a)) :
            		pyttsx3.speak("Opening windows media player")
            		os.system("wmplayer")
            		print("Windows media player successfully opened")	
	#elif (("dont" in a) or ("don't" in a) or ("not" in a) or ("don t" in a) or ("do not" in a) ) :
            		#pyttsx3.speak("Ok I will not open this application")
            		#print("Ok I will not open this application")
	elif ("thank you" in a) :
		pyttsx3.speak("Its my Job")
	elif ("exit" in a) or ("quit" in a) :
		pyttsx3.speak("Visit again Thank you")
		print("Visit again Thank you")
		break
	else :
		pyttsx3.speak("Sorry can't found this application in your system")
		print("Sorry can't found this application in your system !")
		
