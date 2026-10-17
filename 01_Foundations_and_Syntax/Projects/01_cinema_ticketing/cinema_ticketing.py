available = 5
open = True

while open:
    name = input("name:")
    ticket = int(input("ticket"))
    
    if ticket > 0 and ticket <= available:
        print(f"name: {name}, your ticket {ticket}")
        available -= ticket
    elif ticket > available:
        print (f"success{name}bought{available}ticket")
    else:
        print("invalid")
    
    if available == 0:   
        open = False
        print("")
        break 