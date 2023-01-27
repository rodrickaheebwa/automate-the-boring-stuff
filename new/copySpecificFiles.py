import re, os, shutil

#walk through tree
#match regex
#copy to new folder

# create new folder
print('created folder')
#os.makedirs('C:\\Users\\rodri\\Desktop\\New')

# create regex pattern
pattern = re.compile(r"(\.pdf|\.txt)$")

# walk through folder tree
for folderName, subfolders, filenames in os.walk('.'):

    for filename in filenames:
        mo = pattern.search(filename)

        if mo == None:
            continue

        # create path using current folder
        filename = os.path.join(folderName, filename)

        print('moved ' + filename + ' to new folder')
        #shutil.copy(filename, 'C:\\Users\\rodri\\Desktop\\New')
