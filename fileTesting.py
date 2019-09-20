# opening existing file
file = open('C:\\Users\\kjwil\\seven.txt')
file.read()
file.close()
# this will overwrite what is on the current file
file = open('C:\\Users\\kjwil\\seven.txt', 'w')
file.write('Hello Aliens!')
file.close()
file = open('C:\\Users\\kjwil\\seven.txt')
file.read()
# this will append (add) to an existing file

file = open('C:\\Users\\kjwil\\seven.txt', 'a')
file.write('\n\nHello World!')
file.close()
#file.read()

# store complex variables using shelve module. (This will be stored in a binary file)
import shelve

shelfFile = shelve.open('C:\\Users\\kjwil\\avengers.txt')
shelfFile ['Avengers'] = ['Iron Man', 'Hulk', 'Thor', 'Black Widow', 'Captain America']
shelfFile.close()
shelfFile = shelve.open('C:\\Users\\kjwil\\avengers.txt')
shelfFile['Avengers']

import shutil

#copy file to another destination
#shutil.copy('C:\\Users\\kjwil\\seven.txt', 'C:\\Users\\kjwil\\Documents' )

#copy and rename file
#shutil.copy('C:\\Users\\kjwil\\seven.txt', 'C:\\Users\\kjwil\\Documents\\sevenSeven.txt' )

# copy and create a new folder
#shutil.copytree('C:\\Users\\kjwil\\sevens', 'C:\\Users\\kjwil\\seven_backup')

# move file
#shutil.move('C:\\Users\\kjwil\\seven.txt', 'C:\\Users\\kjwil\\seven_backup')

# rename file
#shutil.move('C:\\Users\\kjwil\\seven.txt', 'C:\\Users\\kjwil\\eight.txt')

# deleting file

import os
# delete file
#os.unlink('eight.txt')

# will only delete if the directory is empty
#os.rmdir('C:\\Users\\kjwil\\eight.txt')

# this will delete everything in that directory!!
#shutil.rmtree('C:\\Users\\kjwil\\eight.txt')

for filename in os.listdir():
    if filename.endswith('.txt'):
        #os.unlink(filename)
        print(filename)

# looping through a directory

for folderName, subfolders , fileName in os.walk('C:\\Users\\kjwil'):
    print('The folder is ' + folderName)
    print('The subfolder in ' + folderName + ' are ' + str(subfolders))
    print('The file name in ' + subfolders + ' are ' + str(fileName))
    print()

    

