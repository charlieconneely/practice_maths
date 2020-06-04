# Charlie Conneely 03/06/2020
# Application to practice randomly generated sums

import random

def main(level):

    choice = menu()

    if (level == 1):
        first_num = random.randint(1, 10)
        second_num = random.randint(1, 10)
    elif (level == 2):
        first_num = random.randint(1, 20)
        second_num = random.randint(10, 30)
    elif (level == 3):
        first_num = random.randint(40, 110)
        second_num = random.randint(80, 200)
    elif (level == 4):
        first_num = random.randint(500, 1000)
        second_num = random.randint(700, 1200)

    if (choice == 'a'):
        answer = first_num + second_num
        input_ans = add(first_num, second_num)
    elif (choice == 'b'):
        answer = first_num - second_num
        input_ans = subtract(first_num, second_num)
    elif (choice == 'c'):
        answer = first_num * second_num
        input_ans = multiply(first_num, second_num)

    if (input_ans == answer):
        print("correct!")
    else:
        print("incorrect!")

    while True:
        final_choice = int(input("\nWould you like to:\n1.) Try again" +\
                "\n2.) Try again and change difficulty\n3.) Finish\n"))
        if final_choice == 1 or final_choice == 2 or final_choice == 3:
            break

    return final_choice

def menu():
    menu_choice = input("\nWould you like to \na.) Add\nb.) " + \
            "Subtract\nc.) Multiply\n")
    return menu_choice

def add(n1, n2):
    ans = int(input("\nwhat is " + str(n1) + " plus " + str(n2) + "?\n"))
    return ans

def multiply(n1, n2):
    ans = int(input("\nwhat is " + str(n1) + " times " + str(n2) + "?\n"))
    return ans

def subtract(n1, n2):
    ans = int(input("\nwhat is " + str(n1) + " minus " + str(n2) + "?\n"))
    return ans

if __name__ == "__main__":
    while True:
        level = int(input("\nSelect your difficulty level:\n" + \
                "1.) Easy\n2.) Medium\n3.) Hard\n4.) Extreme\n"))
        while True:
            choice = main(level)
            if choice == 2 or choice == 3:
                break
        if choice == 3:
            break

