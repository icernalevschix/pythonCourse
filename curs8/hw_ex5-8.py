# 1. Write a program that will count number of lines in a file

print('Number of lines in the file: {}'.format(len(open('ex1.txt').readlines())))


# 2. Write a program that will count frequency of a word in a file

word = input("Please enter the word that frequency will be calculated for: ")

# word_count = {}
with open('ex1.txt', 'r') as f:
    text = f.read().lower().split()
    print("Word frequency: {}".format(text.count(word.lower())))

# 2nd method -- 

    # text = f.read().lower()

    # for w in text.split():
    #     word_count[w] = word_count.get(w, 0) + 1

    # print("Word frequency: {}".format(word_count.get(word, 0)))


# 3. Write a program that will append new content to the end of a file.

with open('ex1.txt', 'a') as f:
    f.write("# 3. Write a program that will append new content to the end of a file.\n")


# 4. Write a program that will remove newline character from a file.

with open('ex3.txt', 'r+') as f:
    new_text = f.read().replace('\n', '')
    f.seek(0)
    f.write(new_text)