
"To Do: Task1:Modify the code below to:"
# Read the contents of your file (yourName.txt) by replacing the "w" mode after the file path
# That is replace the write() method with the read method()

"Syntax :  varName = openMethod('pathtofolder/parthtofile/Part7_Dict_DataFiles/fileName.txt', 'w')"
filePath1 = open(
    "Python/Part7_Dict_DataFiles/1_FileHandling_ReadWriteStartFiles/file.txt", "r")
print(filePath1.read())
print(filePath1.readline())  # reads FIRST line
# reads all the text and outputs the text in a list with \n as well, below
print(filePath1.readlines())
filePath1.close()

"Further reading"
# https://www.w3docs.com/snippets/python/how-to-read-a-text-file-into-a-list-or-an-array-with-python.html

# ??
# my_file = open('C:/Users/Ahmet/Desktop/Web Dev Stuff/JustIT-Bootcamp/Python/Part7_Dict_DataFiles/1_FileHandling_ReadWriteStartFiles/DummyFile.txt', 'r')
# my_file.read()
# my_file.close()
