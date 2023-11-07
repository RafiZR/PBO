#open a file
file1 = open("umc.txt", "r")

#read
read_content = file1.read()
print(read_content)

#close
file1.close