"""
Session objectives
●	Write to text files
●	Read data from a text file
●	Append to text files
●   Use context manager to handle resource usage
Key vocabulary
Data files, text files

"""
"Spend 3 minutes to read the comments in green"
# In order to read the data stored in a text file, you must open it first. ​

# Just like a book. You can’t read what is inside if you don’t open it first.​

# There are four modes for opening a file:​

# r for only reading files​

# w for only writing to files​ and creating the file if it does not exists but overwrites existing file contents

# a for adding to an existing file​

# r+ for reading and writing files

"""
Key file-handling techniques are:Open, Read ,Close, Write, Append
The text file must be saved in the same location as your Python file for the program to work. 
"""

"1_FileHandling_ReadWrite/myfile.txt", "w"
"Syntax :  varName = openMethod('pathtofolder/parthtofile/Part7_Dict_DataFiles/fileName.txt', 'w')"
# folder/folder/filename
# filePath1 = open(
#     "'pathtofolder/parthtofile/Part7_Dict_DataFiles/fileName.txt', 'w'")
# filePath1.write("Python Programming with Man4")
# filePath1.close()

filePath1 = open(
    "Python/Part7_Dict_DataFiles/1_FileHandling_ReadWriteStartFiles/file.txt", "w")
filePath1.write("Python Programming updated")
filePath1.close()


# ('pathtofolder/parthtofile/Part7_Dict_DataFiles/fileName.txt', 'w')
# ("Python programming")  # write to file
# close the filepath and file/ releasing the resource


"To Do: Task1: Create a file called yourName.txt and Write your name to the file"
my_file = open(
    'Python/Part7_Dict_DataFiles/1_FileHandling_ReadWriteStartFiles/YourName.txt', 'w')
my_file.write("Ahmet")
my_file.close()


# try:
#     with open('pathtofolder/parthtofile/Part7_Dict_DataFiles/fileName.txt', 'x') as my_file:
#         # Do something with the file, e.g. write to it
#         my_file.write('Hello, world!')
# except FileExistsError:
#     # Handle the case where the file already exists
#     print('File already exists.')


# If stuck refer to the example above
"Further reading"
# https://www.w3docs.com/snippets/python/how-to-read-a-text-file-into-a-list-or-an-array-with-python.html
