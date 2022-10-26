from os import system

receipt_boundary = "-" * 50

def medicine():
    for number in range(1, 1000):
        yield f'M - {number}'

def perfumes():
    for number in range(1, 1000):
        yield f'P - {number}'

def cosmetics():
    for number in range(1, 1000):
        yield f'C - {number}'

m = medicine()
p = perfumes()
c = cosmetics()

# Python Decorator
def customer_ticket(user_selection):
    system("cls")
    print(receipt_boundary)
    print("Sweet's Emporium ticketing system")
    print(receipt_boundary)
    print("Your ticket number is: ")
    if user_selection == 'm':
        print(next(m))
    elif user_selection == 'p':
        print(next(p))
    else:
        print(next(c))
    print("Someone from that section will be with you shortly")
    print(receipt_boundary)
    print("Press 'Enter' to print your ticket")
    print(receipt_boundary)
    input()
    system('cls')
