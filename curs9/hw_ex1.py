"""Project “Quiz generator”
Write a program that will generate question for guessing countrie’s capital with 4 options of answers
1. Read content of file countries.txt and create a dictionary with country as it’s key and capital as value
2. Use random module (import random) in order to get country and it’s capital,using same method get another 3 capitals
3. Generate question with 4 options of answer
4. Prompt user for correct answer and display after correct result"""

import random
import winsound
 
def print_question(rand_list, country):

    print("\nThe capital of {} is: ".format(country))
    print("1. {}".format(rand_list[0]))
    print("2. {}".format(rand_list[1]))
    print("3. {}".format(rand_list[2]))
    print("4. {}".format(rand_list[3]))

    return int(input("\nPlease answer with 1, 2, 3 or 4: "))

def generate_question(country_dict):

    country, capital = random.sample(country_dict.items(), 1)[0]
    rand_list = random.sample(list(country_dict.values()), 3)
    rand_list.insert(random.randrange(0,4), capital)

    return country, capital, rand_list

def main():

    country_dict = {}

    with open('countries.txt', 'rb') as f:
        for i in f.readlines():
            x = i.decode().split(',')
            country_dict[x[0]] = x[1].rstrip('\n')

        while True:
            country, capital, rand_list = generate_question(country_dict)
            choice = print_question(rand_list,country)

            if rand_list[choice-1] == capital:
                print("\nGood Boy !")
                winsound.Beep(500, 1000)
            else:
                print("\nLoser !")
                print(f'The correct asnwer was: {capital}')
                winsound.PlaySound('SystemQuestion', winsound.SND_ALIAS)

if __name__ == '__main__':
    main()