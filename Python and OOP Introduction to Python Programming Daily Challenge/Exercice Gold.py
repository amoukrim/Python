def season():
    
    number = int(input("Entrez un chifre entr 1 et 12 "))
                 
    if number in [9,10,11]:
        print("Autumn")
    elif number in [12,1,2]: 
        print("Winter")
    elif number in [3,4,5]: 
        print("Spring")
    elif number in [6,7,8]:
        print("summer")
season()

