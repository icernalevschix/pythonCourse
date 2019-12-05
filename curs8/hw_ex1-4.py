"""1. Create new folder with name my_data_folder
2. Change path to new created folder
3. Create inside new folder one file and write there user input data about:
Age, occupation, age, height
4. Copy content of file created in ex. 3 in new file (open file in write mode)"""

import os

class Student:

    def __init__(self):
        self.name = input("\nName: ")
        self.surname = input("Surname: ")
        self.age = int(input("Age: "))
        self.occupation = input("Occupation: ")

    def get_st_data(self):
        return f'Name: {self.name}' \
            f'\nSurname: {self.surname}' \
            f'\nAge: {self.age}' \
            f'\nOccupation: {self.occupation}\n\n' 

os.mkdir('my_data_folder')
cd = os.getcwd()

student_list = []

while True:
    new_st = Student()
    student_list.append(new_st)

    if (input("Do you want to add a new student (Y/N): ")).lower() == 'n':
        break

with open(os.path.join(cd,'my_data_folder\\file1.txt'), 'w') as f:
    for i in student_list:
        f.write(i.get_st_data())

with open(os.path.join(cd,'my_data_folder\\file1.txt'), 'r') as rf:
    with open(os.path.join(cd,'my_data_folder\\file2.txt'), 'w') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)

# os.system('copy ' + os.path.join(cd,'my_data_folder\\file1.txt ') + os.path.join(cd,'my_data_folder\\file2.txt'))