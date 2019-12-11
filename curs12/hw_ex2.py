""" 2. Write a program which randomly picks an integer from 1 to 100. Your program
should prompt the user for guesses – if the user guesses incorrectly, it should
print whether the guess is too high or too low. If the user guesses correctly,
the program should print how many guesses the user took to guess the right
answer. You can assume that the user will enter valid input. """

from random import randint

n = randint(1,100)
x = int(input("Please enter a value: "))
i = 0 

while True:
    if x == n:
        i+=1
        break
    elif x > n:
        x = int(input("please try again (less) "))
        i+=1
    else:
        x = int(input("please try again (greater) "))
        i+=1

print('Total number of tries: {}'.format(i))