import tkinter as tk
import sys

#hex_num = input("Enter a Hex Number Watney: ")[:2]
#not_allowed_chars = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19"]
messageArray = []
letArray = []
substring = "x"
allowed_characters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','(',')','$','%','_','/', ' ', ".", "!", ",", ":", "?","'",";","-","+","*"]
hex_allowed_chars=["1","2","3","4","5","6","7","8", "9", "A","a","B","b","C","c","D","d","E","e","F","f"]
print("Initializing...")
print("Hey Watney! Nice of you to try and communicate with us.")
print("You shouldn't have numbers from 1-1F or anything higher than 7F: ")
def hex_to_words():
    # hex_num = input("Enter a Hex Number Watney: ")
    # print(hex_num)
    # while hex_num not in ("Stop", "stop"):
    #     if len(hex_num) <= 2:
    #         letter = chr((int(hex_num,16)))
    #         print(letter)
    #         if any(x not in allowed_characters for x in letter):
    #             print("error: invalid number")
    #             hex_to_words()
    #         else:
    #             letArray.append(letter)
    #             print(letArray)
    #             hex_to_words()
    #     elif len(hex_num) > 2:
    #         print("Keep the number to two digits Watney!")
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
            hex_to_words()
        elif hex_num.lower() == "sentence":
            print(" ".join(messageArray))
        else:
            if len(hex_num) <= 2:
                if any(x not in hex_allowed_chars for x in hex_num):
                    print("condi11")
                    print("error: invalid number")
                    hex_to_words()
                print("condi1")
                letter = chr((int(hex_num,16)))
                print(letter)
                if any(x not in allowed_characters for x in letter):
                    print("condi11")
                    print("error: invalid number")
                    hex_to_words()
                else:
                    print("condi12")
                    letArray.append(letter)
                    print(letArray)
                    hex_to_words()
            elif len(hex_num) > 2:
                print("Keep the number to two digits Watney!")  
 

hex_to_words()
#print(chr((int(hex_num,16)))) 
#print(chr(65))