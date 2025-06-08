#Exercise 1 : Hello World
print("Hello world"*4)
#Exercise 2 : Some Math
result = (99 ** 3) * 8
print(result)
#Exercise 3 : What’s your name ?
my_name = "Moukrim"  
user_name = input("What is your name? ")

if user_name.strip().lower() == my_name.lower():
    print("WAW ! We have the same name! May be we are from the same Family 😄")
else:
    print(f"Nice to meet you, {user_name}!")
#Exercise 4 : Tall enough to ride a roller coaster

seuil = 145
yourheight = int(input("What is your height in centimeters?"))
if seuil<= yourheight :
    print("are tall enough to ride")
else :
    print("are not tall enough, you need to grow some more to ride")
 
#Exercise 5 : Favorite Numbers
    
my_fav_numbers = {12,23,3,45,67,6,90}
print("Mes nombres favoris :", my_fav_numbers)
#Add two new numbers to the set
my_fav_numbers.add(56)
my_fav_numbers.add(50)
#Remove the last number you added to the set
my_fav_numbers.discard(50)
friend_fav_numbers = {2,14,23,47,16,9,3}
print("Nombres favoris de l'ami :", friend_fav_numbers)
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("Nos nombres favoris combinés :", my_fav_numbers)

#Exercise 6: Tuple
 #un tuple est immuable. Si tu veux "modifier", tu dois le recréer
montuple =(2, 4,8,10 ) 
#montuple[2] = 7 # ceci génère une erreur
montuple = montuple+(9,)
print(montuple)#la recréation marche! 

#Exercise 7: List Manipulation
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#Remove "Banana" from the list.
basket.remove("Banana")
#Remove "Blueberries" from the list.
basket.remove("Blueberries")
#Add "Kiwi" to the end of the list.
basket.append("Kiwi")
#Add "Apples" to the beginning of the list.
basket.insert(0,"Apples")
#Count how many times "Apples" appear in the list.
basket.count("Apples")
#Empty the list.
basket.clear
#Print the final state of the list.
print("the final basket",basket)

#Exercise 8 : Sandwich Orders
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
#remove all occurrences of Pastrami sandwich
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
print("sandwich_orders", sandwich_orders)
#Create an empty list called finished_sandwiches.
finished_sandwiches = []
#One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)  # on enlève le premier sandwich
    print(f"I made your {sandwich}")
    finished_sandwiches.append(sandwich)

print("finished_sandwiches",finished_sandwiches)

    



    
    
    
    
           