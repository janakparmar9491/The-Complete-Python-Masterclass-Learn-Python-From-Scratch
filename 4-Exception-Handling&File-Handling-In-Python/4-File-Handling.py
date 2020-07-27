#file = open("demo.txt", 'w')
# do something with the file
#file.close()

# Read file
#fr = open("demo.txt", 'r')
#content = fr.read()
#content = fr.read(10) ## To read 10 bytes
#content = fr.readline()  ## To read first line
#print(content)
#fr.close()

#write to a file
file = open("demo.txt", 'w')
file.write("This is the first text written to the file")
file.close()

"""file = open("demo.txt", 'r')
content = file.read()
print(content)
file.close()"""

file = open("demo.txt", 'a')
file.write("\nThis is the second text written to the file")
file.close()

file = open("demo.txt", 'r')
content = file.read()
print(content)
file.close()
