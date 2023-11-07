#open file 
file1= open("umc.txt", "r")
teks="praktikum python\n"

file2= open("umc.txt", "a")
file2.write(teks)
file2.close()

#read
read_content =file1.read()
print(read_content)

#close the file
file1.close()
