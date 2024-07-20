import os
current_directory = os.path.abspath(os.path.dirname(__file__))

file  = open(os.path.join(current_directory, 'file', 'a.txt'), "r")

print(file.read())

file.close()
