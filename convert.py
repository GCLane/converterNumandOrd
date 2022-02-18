#Convert program by Grant Lane
#Date: 2-15-22
#Takes in .txt files and then reads then converts numbers to words
#then writes to another .txt file
import sys

numStr_list = ["one","two","three","four","five", "six", "seven", "eight", "nine","ten"]
num_list = ['1','2','3','4','5','6','7','8','9', '10']
ordStr_list = ["first", "second", "third", "fourth", "fifth","sixth", "seventh", "eighth", "ninth", "tenth"]
ord_list = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th"]

infile = sys.argv[1]
outfile = sys.argv[2]


#does the writing and reading of the text
def readfile(filename, outfile):
    infile = open(filename, 'r')
    my_file = []
    my_file = infile.readlines()
    infile.close()
    outfile = open(outfile, "w")
    for line in my_file:
        line = convert_text(line)
        outfile.write(line)
    outfile.close()

readfile(infile, outfile) #calls the method that does the work
#converts a cardinal number to the written version
def convert_num(word):
    counter = 0
    while(counter < len(num_list) - 1  and word != num_list[counter]):
        counter += 1
    if(word == num_list[counter]):
        word = numStr_list[counter]
    return word
#converts an ordinal number to the written version
def convert_ord(word):
    counter = 0
    while(counter < len(ord_list) - 1 and word != ord_list[counter]):
        counter += 1
    if(word == ord_list[counter]):
        word = ordStr_list[counter]
    return word
#converts the text to the converted way
def convert_text(line):
    the_list = line.split(' ')
    newline = ""
    for word in the_list:
        if(len(word) == 1 and num_check(word)):
            word = convert_num(word)
        elif(len(word) == 2):
            if(word == "10"):
                word = convert_num(word)
            elif(num_check(word[0]) and (word[1] < "0" or word[1] > '9')):
                word = convert_num(word[0]) + word[1]
        elif(len(word) >= 3):
            if(ord_check(word[0:3])):
                word = convert_ord(word[0:3]) + word[3:len(word)]
            elif(ord_check(word[0:4])):
                word = convert_ord(word[0:4]) + word[4:len(word)]
            elif(num_check(word[0])):
                if(word[0:2] == "10"):
                    word = convert_num(word[0:2]) + word[2:len(word)]
                elif(word[1] < "0" or word[1] > '9'):
                    word = convert_num(word[0]) + word[1:len(word)]
        if(word == the_list[-1]):
            newline += word
        else:
            newline += word + ' '    
    return newline

#runs a check on the text to see if it is a number
def num_check(letter):
    isNum = False
    for i in num_list:
        if(letter == i):
            isNum = True
    return isNum
#runs a check on the text to see if it is an ordinal
def ord_check(ordinal):
    isOrd = False
    for i in ord_list:
        if(ordinal == i):
            isOrd = True
    return isOrd


