file = open("cc6.txt", 'w')
file.write("This is first text in file.")
file.close()

file = open("cc6.txt", 'r')
content = file.read()
print(content)
file.close()

file = open("cc6.txt", 'a')
file.write("\nThis is second text in file.")
file.close()