# walk through folder tree
# locate files or folders larger than 100 MB
# os.path.getsize()
# C:\\Users\\rodri

import os

for folderName, subfolders, filenames in os.walk('E:'):
        for filename in filenames:
            filename = os.path.join(folderName, filename)
            filesize = os.path.getsize(filename)
            if filesize >= 100000000:
                print(filename, filesize)
