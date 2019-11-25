#1. Calculate sum of size all .py files in your working directory. Convert in in MegaBytes.

import os

files = os.scandir('.')

total_size = 0

for f in files:
    if f.is_dir():
        continue
    last_modified_file = f
    last_accessed_file = f
    total_size += f.stat().st_size
    if f.stat().st_mtime > last_modified_file.stat().st_mtime:
        last_modified_file = f
    if f.stat().st_atime > last_accessed_file.stat().st_atime:
        last_accessed_file = f

print("Total size ={} MB".format(total_size/(1024*1024)))

#2. Find name of last modified file in your current working directory.

print("Last modified file: {}".format(last_modified_file.name))

#3. Find name of last accessed filed your current working directory.

print("Last accessed file: {}".format(last_accessed_file.name))

