# There are four modes for opening a file:​

# r for only reading files​

# w for only writing to files​ and creating the file if it does not exists but overwrites existing file contents

# a for adding to an existing file​

# r+ for reading and writing files


# with open("Python/Part7_Dict_DataFiles/1_FileHandling_ReadWriteStartFiles/file2.txt", "r+") as filePath1:  # folder/folder/filename
#     print(filePath1.read())  # read from fuile
#     contents = "\nA\nb\nC\nD\nE\nF"
#     filePath1.write(contents)  # write to file
#     readContents = filePath1.read()
#     print(readContents)


"To Do: Task 1: Modify the code below to"
# Read the contents from your file (yourName.txt) and write to your file by replacing the "w" mode after the file path
# with the correct mode and ensure you use both the read and the write() methods to perform their respective
# operations

with open(
        "Python/Part7_Dict_DataFiles/1_FileHandling_ReadWriteStartFiles/YourName.txt", "r+") as filePath1:
    filePath1.write("\n Edited with r+")
    readContents = filePath1.read()
    print(readContents)
