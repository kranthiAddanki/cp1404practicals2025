from prac_06.guitars import Guitar

guitars = []
print("My guitars!")
name = input("Name:")
while name != "":
    year = int(input("Year:"))
    cost = float(input("Cost:$"))
    guitar_to_add = Guitar(name, year, cost)
    guitars.append(guitar_to_add)
    print(f"{guitar_to_add} added")
    name= input("Name:")

print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    VINTAGE_STRING: str = " "
    if guitar.is_vintage():
        VINTAGE_STRING = "(vintage)"
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {VINTAGE_STRING}")


