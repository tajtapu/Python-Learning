import os
import shutil


for folderName, subfolders, filenames in os.walk('c:\\Users\\taj_t'):
	print('The folder is ' + folderName)
	print('The subfolder in ' + folderName+ ' are: ' + str(subfolders))
	print('The filesname in ' + folderName+ ' are: ' + str(filenames))
	print()


        for subfolder in subfolders:
            if 'fish' in subfolder:
                os.rmdir(subfolder)

        for file in filenames:
            if file.endswith('.txt')
            shutil.copy(os.join (folderName, file),os.join (folderName, file+'.backup'))
