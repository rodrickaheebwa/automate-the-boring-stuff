#renaming images (screenshots) to natural numbers

import os, re

name_pattern = re.compile(r"png$")

for index, file in enumerate(os.listdir('.')):
    mo = name_pattern.search(file)
    if mo:
        new_name = str(index) + ".png"
        try:
            print("renaming")
            # os.rename(file, new_name)
        except:
            print("error")

