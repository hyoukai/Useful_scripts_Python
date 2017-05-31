'''
This script can be used to verify whether all the files inside two directorys (dir1 & dir2) are exactly the same.
@hyoukai
'''

import os 
import filecmp
import string

root1 = './dir1/'
root2 = './dir2/'

for path, subdirs, files in os.walk(root1):
	for name in files:
		file1 = os.path.join(path, name)
		file2 = string.replace(file1, root1, root2)
		if (not filecmp.cmp(file1, file2)):
			print " --- Differences exist between the following two files --- "
			print file1
			print file2
