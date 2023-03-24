name = ""
order = int(0)
MeatLovers = 9.95
Hawaiian = 4.95
VegDelight = 5.95
total = 0

print("################################################")
print("Welcome to PizzaHeaven")
print("Please place order from the following Menu")
print("")
print("MeatLovers:", MeatLovers)
print("Hawaiian:", Hawaiian)
print("VegDelight:", VegDelight)
print("Enter 1 for MeatLovers, 2 for Hawaiian, 3 VegDelight and 0 to finish a Sorder.")
name = input("What is your name ? ")
print("Enter any number between 1 and 3: ")
order = int(input("What is your order? "))



while order != 0:
    if order == 1:
        total = total + 9.95
        order = int(input("What is your order? "))
    if order == 2:
        total = total + 4.95
        order = int(input("What is your order? "))
    if order == 3:
        total = total + 5.95
        order = int(input("What is your order? "))
    if order < 0 or order > 3:
        order = int(input("Enter any number between 1 and 3 or 0 to finish order :"))

print("Your total is: ${:.2f}" .format(total))

print(name, ", Your order will be ready in 5 minutes")
