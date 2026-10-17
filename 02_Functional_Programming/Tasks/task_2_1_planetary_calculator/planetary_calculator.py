def calculate_weight (mass,plant="earth"):
    if plant == "earth":
    
        gravity=9.8
    
    elif plant=="mars":
    
        gravity=3.71
    elif plant=="jupiter":
    
        gravity=24.79
    return mass * gravity

earth_weight = calculate_weight()
    print(f"Weight on Earth: {earth_weight} N")

    
    mars_weight = calculate_weight(, planet="Mars")
    print(f"Weight on Mars: {mars_weight} N")

   
    jupiter_weight = calculate_weight(, "Jupiter")
    print(f"Weight on Jupiter: {jupiter_weight} N")
    
    
    
    
    
    