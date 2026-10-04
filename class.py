snack_name ="chips"
price = 1.50
quantity = 10
is_available = True

print("snack" , snack_name)
print("price: $" ,price)
print("In stock:" , quantity)
print("available?", is_available)

print(type(snack_name))
print(type(price))
print(type(quantity))
print(type(is_available))

Total = price*quantity
print("Total value: $", Total)
print("sales price : $", price==0.25)
print(" Double stock : ", quantity*2)

print(" is price under $2?", price<2)
print("More then 5 in stock ?", quantity>5)
print(" is price is exactly $1.50 ?", price== 1.50)

shop_name = "Quick" + "  " + "Bites"
print("shop name :", shop_name)
print("Letters in  snack name :", len(snack_name))
print(" First letter :", snack_name[0])

price_a = 1.50
price_b = 3.00
print( "Before" , price_a, "and ",price_b)


temp =price_a
price_a=price_b
price_b=temp

print("After", price_a ,"and", price_b)

 



