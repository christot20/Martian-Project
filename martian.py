import tkinter as tk
import sys
import time

messageArray = []
letArray = []
allowed_characters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','(',')','$','%','_','/', ' ', ".", "!", ",", ":", "?","'",";","-","+","*"]
hex_allowed_chars=["1","2","3","4","5","6","7","8", "9", "A","a","B","b","C","c","D","d","E","e","F","f"]
time.sleep(2)
print("Initializing...")
time.sleep(2)
print("Hey Watney! Nice of you to try and communicate with us.")
time.sleep(2)
print("The commands are:" +"\n")
time.sleep(1)
print("Stop: Shuts down program." + "\n"+"Reset: Clears past letters and words."+"\n"+"End: Combines letters to make word."+"\n"+"Sentence: Takes words to formulate message."+"\n"+"Del: Backspace."+"\n")
time.sleep(2)
print("You shouldn't have numbers from 1-1F or anything higher than 7F: ")
#add a delete feature for the writing of letters using pop function
def hex_to_words():
    while True:
        hex_num = input("Enter a Hex Number Watney: ")
        print(hex_num)
        if hex_num.lower() == "stop":
            print("Program shutting down...")
            sys.exit()
        elif hex_num.lower() == "end":
            print(hex_num)
            message = "".join(letArray)
            messageArray.append(message)
            letArray.clear()
            print(messageArray)
            print(letArray)
            hex_to_words()  
        elif hex_num.lower() == "reset":
            messageArray.clear()
            letArray.clear()
            hex_to_words()
        elif hex_num.lower() == "sentence":
            print(" ".join(messageArray))
        elif hex_num.lower() == "del":
            letArray.pop()
        elif hex_num.lower() == "help":
            print("Stop: Shuts down program." + "\n"+"Reset: Clears past letters and words."+"\n"+"End: Combines letters to make word."+"\n"+"Sentence: Takes words to formulate message."+"\n"+"Del: Backspace."+"\n")
        else:
            if len(hex_num) <= 2:
                if any(x not in hex_allowed_chars for x in hex_num):
                    print("error: invalid number")
                    hex_to_words()
                letter = chr((int(hex_num,16)))
                print(letter)
                if any(x not in allowed_characters for x in letter):
                    print("error: invalid number")
                    hex_to_words()
                else:
                    letArray.append(letter)
                    print(letArray)
                    hex_to_words()
            elif len(hex_num) > 2:
                print("Keep the number to two digits Watney!")  

hex_to_words()
