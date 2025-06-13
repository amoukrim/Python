keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

mon_dictionnaire = dict(zip(keys, values))
print (mon_dictionnaire) 

#Exercice 2
def calculprix():
    cost = 0
    family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
    
    for age in family.values() :
        if 3>age<=12:
            cost+= 10
        elif age>12:
            cost+= 15
    print(f"cost: {cost}")    
calculprix()  

brand = {"name": "Zara",
"creation_date": 1975,
"creator_name": "Amancio Ortega Gaona",
"type_of_clothes": ["men", "women", "children", "home"],
"international_competitors": ["Gap", "H&M", "Benetton"],
"number_stores": 7000,
"major_color":{ 
    "France": "blue", 
    "Spain": "red", 
    "US": ["pink", "green"]}
}
brand["number_stores"] = 2
print(f"Zara is for {brand['type_of_clothes']}")
brand["country_creation" ] = "Spain"
if "international_competitor" in brand: 
    brand["international_competitors"].append("Desigual")
print("Last international competitor:", brand["international_competitors"][-1])
