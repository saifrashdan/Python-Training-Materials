available = 200.0
session = True
 
while open :
    amount = float(input(f"available={available}"))
    
    if amount > 0 and amount <= available:
        available -= amount
        print (f"{available}")
    elif amount > available:
        print(f"{amount}")
    else :
        print("erorr")
    
    if available == 0:
        print("available=0")
        session = False
        break 
    