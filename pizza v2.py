name = ""
order = ""
MeatLovers = 9.95
Hawaiian = 4.95
VegDelight = 5.95
total = 0
peperoni = 0.50
onion =0.50
mushroom = 0.50
cheese = 0.50
tomato = 0.50
orders = []

print("Welcome to Pizza Heaven")
print("##################Menu#########################")
print("A. MeatLovers:", MeatLovers)
print("B. Hawaiian:", Hawaiian)
print("C. VegDelight:", VegDelight)

print("#################Toppings######################")
print("P. peperoni",peperoni)
print("O. onion",onion)
print("M. mushroom",mushroom)
print("CH. cheese",cheese)
print("T. tomato",tomato )

print("###############################################")

name = input("What is your name? ")
print("Enter any letter between A and C to order a pizza, or 0 to finish order: ")

while order != "0":
    order = input("What is your order? ").lower()
    if order == "a":
        orders.append("MeatLovers")
        total += MeatLovers
        print("Added MeatLovers to your order. Total: $", total)
    elif order == "b":
        orders.append("Hawaiian")
        total += Hawaiian
        print("Added Hawaiian to your order. Total: $", total)
    elif order == "c":
        orders.append("VegDelight")
        total += VegDelight
        print("Added VegDelight to your order. Total: $", total)
    elif order == "p":
        orders[-1] += ", peperoni"
        total += peperoni
        print("Added peperoni to your order. Total: $", total)
    elif order == "o":
        orders[-1] += ", onion"
        total += onion
        print("Added onion to your order. Total: $", total)
    elif order == "m":
        orders[-1] += ", mushroom"
        total += mushroom
        print("Added mushroom to your order. Total: $", total)
    elif order == "ch":
        orders[-1] += ", cheese"
        total += cheese
        print("Added cheese to your order. Total: $", total)
    elif order == "t":
        orders[-1] += ", tomato"
        total += tomato
        print("Added tomato to your order. Total: $", total)
    elif order not in ["a", "b", "c", "p", "o", "m", "ch", "t", "0"]:
        print("Invalid input. Please enter any letter between A and C or 0 to finish order.")
        continue

print("Your order is:")
for i, o in enumerate(orders, start=1):
    print(i, ".", o)

print("Your total is: ${:.2f}".format(total))
print(name, ", Your order will be ready in 5 minutes.")
