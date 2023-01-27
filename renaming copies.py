import os, re

name_pattern = re.compile(r"^(Copy of )((\w|\s)+)")

for file in os.listdir('.'):
    mo = name_pattern.search(file)
    if mo:
        new_name = mo.group(2) + 'p' + '.py'
        try:
            print("renaming")
            #os.rename(file, new_name)
        except:
            print("error")
