from os import system

def customer_ticket(user_selection):
    system("cls")
    def store_banner():
        system("cls")
        print("Sweet's Emporium")
        print("Your Number is: ")
        user_selection()
        print("Someone will be with you shortly")
    return store_banner

@customer_ticket
def medicine():
    print("Medicine number")

@customer_ticket
def perfumes():
    print("Perfume number")

@customer_ticket
def cosmetics():
    print("Cosmetic number")
