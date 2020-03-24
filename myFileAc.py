#! python3
# myFileAc.py  - This prog will read,and append some text to file
f = open("TestFile.txt","rt")
# print(f.read())   Read entire file
print(f.read(20))     # Read first 20 bytes
print(f.readline())  # Read first line of file from cursor position
print(f.readline())  # read 2nd line of the file from cursor position

# Close the file and read the file once again
f.close()
f = open("TestFile.txt","rt")
print(f.read(20))     # Read first 20 bytes
f.close()

# Open the file and read line by line for entire file

f = open("TestFile.txt","rt")
for x in f:
    print(x)
f.close()

# Append some test to the file
f = open("TestFile.txt", "at")
f.write("The File got changed by Abhishek")
f.close()


