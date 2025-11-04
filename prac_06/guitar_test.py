from prac_06.guitars import Guitar

guitar = Guitar("Gibson L-5 CES",1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013, 1500.00)
# print(guitar)
# print(another_guitar)

print(f"{guitar.name} get_age() - Expected 103. Got {guitar.get_age()}")
print(f"{another_guitar.name} get_age() - Expected 12. Got {another_guitar.get_age()}")
print(f"{guitar.name} get_age() - Expected TRUE. Got {guitar.is_vintage()}")
print(f"{another_guitar.name} get_age() - Expected FALSE. Got {another_guitar.is_vintage()}")

