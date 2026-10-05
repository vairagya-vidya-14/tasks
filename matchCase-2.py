print("-------MENU-------")
print("1.Biryani")
print("2.chicken 65")
print("3.Veg Pulao")
print("4.Butter Chicken")
print("5.Panner Tikka")
choice=int(input("enter your choice:"))
match choice:
    case 1:
        print("Item : Biryani")
        print("price: 250/-")
        print("Description: Fragrant basmati rice cooked with spices and chicken.")
    case 2:
        print("Item : Chicken 65")
        print("price: 180/-")
        print("Description: Crispy and spicy deep-fried chicken pieces.")
    case 3:
        print("Item : Veg pulav")
        print("price: 220/-")
        print("Description: Fragrant basmati rice cooked with spices and veggies.")
    case 4:
        print("Item : Butter chicken")
        print("price: 300/-")
        print("Description: Creamy, buttery, rich, flavorful chicken curry.")
    case 5:
        print("Item : Paneer Tikka")
        print("price: 200/-")
        print("Description: Grilled paneer cubes marinated with spices and yogurt.")
    case _:
        print("Sorry not available🙃")
