items = {
    "burger" : 500,
    "pizza" : 700,
    "biriyani" : 900,
    "egg chilli" : 10000
}
purchase = 0
print("Welcome to XYZ Shop")
print("========================")
print("Menu")
print("========================")
for item , price in items.items():
  print(f"{item.title()} : Rs {price}")
print("")

print("Type 'done' if you finished ordering!")
print("")

while True:
  item = input("Enter what do you want to buy :")

  if item == 'done':
    break
  elif item in items:
    purchase +=items[item]
  else:
    print("Item not available. Please choose from the menu")

if purchase > 10000:
  purchase -= purchase * 0.10
elif purchase > 2000:
  purchase -= purchase * 0.07
elif purchase > 1000:
  purchase -= purchase * 0.05

print("Total Amount:",purchase)


