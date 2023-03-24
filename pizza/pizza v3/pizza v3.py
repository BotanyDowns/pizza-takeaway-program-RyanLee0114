#This pizza program uses Try and Except, While loop and dictionary of items
#setting variables.
menu={'a':5.95, 'b':4.95, 'c':3.95, 'd':5.35}
name = ""
more = "s"
qty = int(0)
total = 0
orders = []
print ('Welcome to Pizza Haven')
print('Please place order from the following menu')
with open('pizzamenu.txt', 'r') as f:
    read_content = f.read()
    print (read_content)
print('')

name = input('Enter your name : ')

while more != 'n':
    item = input('Enter item number: ').lower()
    if item not in menu:
        print('this item is not in menu.')
        item = input('Enter item number: ').lower()
    try:
        qty = int(input('Enter quantity required : '))
    except ValueError:
        print ('please enter positive numbers only')
        qty = int(input('Enter quantity required : '))
    price = menu[item]
    linetotal=price*qty
    total = total+linetotal
    if item == "a":
        x= "meatlover"
    if item == "b":
        x= "hawaiian"
    if item == "c":
        x= "vegdelight" 
    if item == "d":
        x= "chicken"
    order= x,qty
    orders.append(order)
    print('your total is : ${:.2f}'.format(total))
    more = input('would you like another item? : ').lower()
    if more =="no":
        break
for i, o in enumerate(orders, start=1):
    print(i, ".", o)
print(name,'your total is : ${:.2f}'.format(total))

