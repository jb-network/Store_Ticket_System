import numbers
from os import system

menu_selection = 0
menu_boundary = "*" * 50

while menu_selection != 4:
    print(menu_boundary)
    print("Welcome to Sweet's Emporium")
    print(menu_boundary)
    print("Please choose the section that you are here to visit:")
    print("1. Medicine")
    print("2. Perfumes")
    print("3. Cosmetics")
    print("4. Exit")
    print(menu_boundary)
    menu_selection = int(input("Your Selection (1-4): "))

    if menu_selection == 1:
        numbers.customer_ticket("m")
    elif menu_selection == 2:
        numbers.customer_ticket("p")
    elif menu_selection == 3:
        numbers.customer_ticket("c")
    elif menu_selection == 4:
        print(menu_boundary)
        exit("Thanks for shopping at Sweet's Emporium")
        print(menu_boundary)
    else:
        print (menu_boundary)
        print("The number you selected is not valid")
        input("Press enter to make a valid selection")
        print(menu_boundary)
        system("cls")
