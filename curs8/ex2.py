import os

current_directory = os.getcwd()
join_path = os.path.join(current_directory,'my_folder')
print(join_path)

folder_content = os.listdir(join_path)
print(folder_content)

print(os.path.abspath('.'))
print(os.path.abspath('./my_folder'))
print(os.path.abspath('../my_folder'))

rel_path = os.path.isabs('.')
abs_path = os.path.isabs(os.path.abspath('.'))
print(rel_path)
print(abs_path)

path = '.'
files = os.scandir(path)
for f in files:
    # print('name:', f.name, 'path:', f.path)
    # print('is file', f.is_file(), 'is directory', f.is_dir())
    info = f.stat()
    print(info.st_size)