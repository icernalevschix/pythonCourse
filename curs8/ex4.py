import os

path_1 = 'my_folder'
path_2 = 'my_folder_2'

dir_exists = os.path.exists(path_1)
dir_dont_exists = os.path.exists(path_2)

print(os.path.abspath('.'))
print(dir_exists)
print(dir_dont_exists)

dir_path = 'my_folder'
file_path = 'ex1.py'

is_dir = os.path.isdir(dir_path)
print(is_dir)

is_dir = os.path.isdir(file_path)
print(is_dir)

# os.mkdir('new_folder')
os.rmdir('new_folder')
# os.remove('test.txt')