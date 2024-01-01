#!/usr/bin/python3
import random


random_number = random.randint(1, 100)
stopper = 1

def print_welcome():
    green_color = "\033[92m"
    reset_color = "\033[0m"
    print(green_color + r'''
   _____ _              _      _____ _           _       
  / ____| |            | |    / ____| |         | |      
 | |    | |__   __ _ __| |   | |    | |__   __ _| |_ ___ 
 | |    | '_ \ / _` / _` |   | |    | '_ \ / _` | __/ _ \
 | |____| | | | (_| \__ \   | |____| | | | (_| | ||  __/
  \_____|_| |_|\__,_|___/    \_____|_| |_|\__,_|\__\___|
                                                        
    ''')
    print("Welcome to Guess the Number!")
    print("Try to guess the secret number I'm thinking of.")
    print("Let's see if you can get it right!\n" + reset_color)

def find_half(number):
    if number < 50:
        print("its less than 50")
    else:
        print("its more or equal to 50")

def find_modulo_two(number):
    if number % 2 == 0:
        print("it can be divided by 2")
    else:
        print("its not divided by 2")

def find_modulo_three(number):
    if number % 3 == 0:
        print("it can be divided by 3")
    else:
        print("its not divided by 3")

def find_modulo_five(number):
    if number % 5 == 0:
        print("it can be divided by 5")
    else:
        print("its not divided by 5")

def find_modulo_ten(number):
    if number % 10 == 0:
        print("it can be divided by 10")
    else:
        print("its not divided by 10")

def hint_giver(number, counter):
    if counter == 1:
        find_half(number)
    if counter == 2:
        find_modulo_two(number)
    if counter == 3:
        find_modulo_three(number)
    if counter == 4:
        find_modulo_five(number)
    if counter == 5:
        find_modulo_ten(number)

hints_counter = 0
def check_input(guess):
    tries_counter = 0
    try:
        guess = int(guess)
        if guess == random_number:
            if tries_counter == 0:
                print("Damns! You won from the first try!!")
            else:
                print("Your guess is right!")
            return 0
        else:
            tries_counter = tries_counter + 1
            answer = input("Its not the correct answer!\nDo you want a hint ? please Press YES or No\n")
            if answer == "YES":
                hints_counter = hints_counter + 1
                if hints_counter > 5:
                    print("You passed the number of tries!\nGAME OVER\n")
                    return 0
                hint_giver(guess, hints_counter)
        return 1
    except ValueError:
        print("choose a valid 1 to 100 number!!!")
        return 1

print_welcome()
while stopper:
    guess = input()
    print("to check this is the random " + str(random_number))
    stopper = check_input(guess)


