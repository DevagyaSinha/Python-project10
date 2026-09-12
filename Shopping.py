# Shopping List Manager

# Open the file in append mode
file = open("shopping.txt", "a")

item = input("Enter an item to add: ")

# Add the item to the file
file.write(item + "\n")

file.close()

# Read the updated shopping list
file = open("shopping.txt", "r")

print("\nUpdated Shopping List:")

for item in file:
    print(item.strip())

file.close()