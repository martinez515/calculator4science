# This is the Project:  Shooping for sciense

# cost of supplies

flowerpot_price = 4.00
flower_seeds_price = 1.00
soil_price = 2.00

#Prints menu and prices
print("         MENU       \n " )
print(" Flower pots   $4.00 " )
print(" Flower seeds  $1.00 " )
print(" Bag of soil   $2.00 \n" )

# Shooping list / items

#INPUT

flowerpot = int(input("How many flowerpots you need?  "))
flower_seeds = int(input("How many packs of seeds do you need?  "))
soil = int(input("How many bags of soil do you need?  "))
print()

# Enter budget

budget = float(input("How much money do you have to pay for your supplies?  "))

tax_rate = 0.0875

# Calculate cost

cost_of_items = (flowerpot * flowerpot_price) + (flower_seeds * flower_seeds_price) + (soil * soil_price)
total_cost = round(cost_of_items * tax_rate) + cost_of_items


#OUTPUT
changeback = round((budget - total_cost),2)
print()
print(f"your total is {total_cost}")
print()
print(f"Here is your change...{changeback}")
