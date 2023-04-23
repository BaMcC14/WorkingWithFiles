#Opening up the file
fhandler = open('poems.txt')
print(fhandler)
print("----------")

#Opening up the file and counting the lines inside.
fhandler = open('poems.txt')
count = 0
for line in fhandler:
  count = count + 1
print("Line Count: ", count)
print("----------")

#Printing the conets of the file
fhandler = open('poems.txt')
text = fhandler.read()
print(text)

#Creating and Writing to a file 
fout = open('output.txt', 'w')
line1 = "Putting in a line of text,\n"
fout.write(line1)
fout.close()






