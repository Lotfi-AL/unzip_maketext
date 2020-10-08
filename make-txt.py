import os,sys

path = os.walk(".")

data_to_write = []
with open("retting.txt","r") as file:
    for line in file:
        data_to_write.append(line)

#traverse through the directories in the current directory which this file is placed in write everything that is in data_to_write to
#a .txt file 
for root, directories, files in path:
    for directory in directories:
        #completename is root + what you want to name the file
        completeName = os.path.join(root,"retting.txt")
        with open (completeName,"w") as file:
            file.writelines(data_to_write)