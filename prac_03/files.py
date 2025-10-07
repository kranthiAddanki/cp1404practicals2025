#1.
# name = input("enter your name:")
# out_file =open("name.txt", "w")
# print(name, file =out_file)
# out_file.close()

#2.


#3.
# in_file = open("numbers.txt", "r")
# in_file.readlines(2)


score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score < 50:
    print("Bad")
elif score < 90:
    print("Passable")
else:
    print("Excellent")







