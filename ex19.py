def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count}!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_crackers = 50
amount_of_cheese = 10

cheese_and_crackers(amount_of_cheese, amount_of_crackers)#variables as arguments

print("we can even do math inside too: ")
cheese_and_crackers(10+20, 5+6)

print("And we can combine the two , variables anf math:")
cheese_and_crackers(amount_of_cheese +100, amount_of_crackers + 1000)
