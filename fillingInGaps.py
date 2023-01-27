#! python3
# Renames files of a certain pattern in an orderly manner

# create regex to identify pattern e.g. spam001...
# find all files with this pattern in a folder
# sort files in order of name
# find missing names(numbers)
# rename accordingly starting from the missing number

import os, shutil, re

# create regex pattern
fileNamePattern = re.compile(r"^(spam)(\d\d\d)(\.txt)$")

# loop over the files in the working directory
for fileName in os.listdir('.'):
    mo = fileNamePattern.search(fileName)

    if mo == None:
        continue

    numberPart = mo.group(2)

    # strip leading zeros
    # for loop using total number of matched files
    # if not equal to number, change accordingly
