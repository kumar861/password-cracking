#!/usr/bin/python3
import os

filename = input("Enter the 7zip file: ")
filename = str(filename)
wordlist = input("Enter the wordlist: ")
wordlist = str(wordlist)
f = open(wordlist,'r')
l = f.read().splitlines()
0
for word in l:
    x = os.system('7z -y e -p{0} {1} > /dev/null 2> /dev/null'.format(word, filename ))
    if x == 0:
        print("password found " + word)
    else:
        print("password not working " + word)
