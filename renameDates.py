#! python3
# Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY.

#Create a regex that can identify the text pattern of American-style dates.
#Call os.listdir() to find all the files in the working directory.
#Loop over each filename, using the regex to check whether it has a date.
#If it has a date, rename the file with shutil.move().

import os, shutil, re

# create regex that matches files with American date format
datePattern = re.compile(r""" ^(.*?)
                ((0|1)?\d)-
                ((0|1|2|3)?\d)-
                ((19|20)\d\d)
                (.*?)$
              """, re.VERBOSE)

# loop over the files in the working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # skip files without a date
    if mo == None:
        continue

    # get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # form European-style filename
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # get the full absolute file paths
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # rename the files
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))

    #shutil.move(amerFilename, euroFilename)

##############################################
#improve regex so that before part doesn't end with number and after part doesn't start with number
