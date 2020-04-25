eventName = input("Enter event name: ")
foodName = input("Enter food name: ")
people = []
temp = input("Enter name of person sharing this food: ")
people.append(temp)

addAnother = input("Add another person to this dish? (Y/N): ")

while (addAnother != "n" and "N"):
  
  temp = input("Enter name of person sharing this food: ")
  people.append(temp)
  addAnother = input("Add another person to this dish? (Y/N): ")
  
print(people)