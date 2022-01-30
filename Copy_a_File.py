# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination + destination can be a directory
# copy2() = copies metadata (file's creation and modification times)

import shutil

shutil.copyfile('test.txt','copytest.txt')
#or
shutil.copyfile('test.txt','C:\\Users\\kelliethomsen\\Desktop\\copytest.txt')
