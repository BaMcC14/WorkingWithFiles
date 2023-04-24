#Challenge 3.3.4
#Working with files in Python

#Opening up the file
#fhandler = open('poems.txt')
#print(fhandler)
#print("----------")

#Opening up the file and counting the lines inside.
#fhandler = open('poems.txt')
#count = 0
#for line in fhandler:
#  count = count + 1
#print("Line Count: ", count)
#print("----------")

#Printing the conets of the file
#fhandler = open('poems.txt')
#text = fhandler.read()
#print(text)

#Creating and Writing to a file 
#fout = open('output.txt', 'w')
#line1 = "Putting in a line of text,\n"
#fout.write(line1)
#fout.close()

#Challenge 3.3.5
#Reading and Writing to files

#fout = open('firstexample.txt', 'w')
#fout.write('Putting in a line of text\n')
#fout.close()
#fout = open('firstexample.txt', 'w')
#fout.write('Putting in a line of text\n')
#fout.close()
#fout = open('firstexample.txt', 'w')
#fout.write('Putting in a line of text\n')
#fout.close()
#'w' always opens new files and if the new files exist it will clear the data in that file
#This code if for 3 lines of text with in the new firstexample.txt file but only writes one line

#fout = open('firstexample.txt', 'a')
#fout.write('Putting in a line of text\n')
#fout.close()
#'a' appends to a file. Everytime it is executed it will append the new text.

#Reading data from a file

fout = open('myFile.txt', 'w')
fout.write('My first line of text\n')
fout.write('My second line of text\n')
fout.write('My third line of text\n')
fout.write('My fourth line of text\n')
fout.close()

#fin = open('myFile.txt', 'r')

#for line in fin:
#  print(line)
#print()

#fin.close()

#fin = open('myFile.txt', 'r')

#for line in fin:
#  print(line, end="")
#print()

#fin.close()

#.read() method****
#fin = open('myFile.txt', 'r')

#contents = fin.read()
#print(contents)
#fin.close()

#.readline() method****

#fin = open('myFile.txt', 'r')
#the following statement will read all the lines from the fin file handler and return the lines as a list
#lines = fin.readlines()
#print(lines[0], end="")
#print(lines[1])

#fin.close()


#Outputting with a for loop 
#fin = open('myFile.txt', 'r')
#lines = fin.readlines()
#for line in lines:
#  print(line, end="")

#fin.close()

#fin = open('myFile.txt')

#line1 = fin.readline();
#print(line1, end="")
#line2 = fin.readline();
#print(line2, end="")

#fin.close()


#writing and reading a list to a text file

#names = ["Sophia", "Python"]
#fout = open('names.txt', 'w')
#for m in names:
#  fout.write(m + "\n")

#fout.close()

#names = []
#fin = open('names.txt', 'r')
#for line in fin:
#  line = line.replace("\n", "")
#  names.append(line)
#print(names)

#Writing and reading integers to a file

#years = [1975, 1979, 1983]
#fout = open('years.txt', 'w')
#for year in years:
#  fout.write(str(year) + "\n")
#fout.close()

#years = []
#fin = open('years.txt', 'r')
#for line in fin:
#  line = line.replace("\n", "")
#  years.append(int(line))
#print(years)

#Removing files 
import os
os.remove("years.txt")







