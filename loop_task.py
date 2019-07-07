list_of_items = []
item_name = ""
while item_name != "done":
	item_name = input("item (enter \"done\" when finished): ")
	if item_name == "done":
		break
	price = float(input("item (enter \"done\" when finished): "))
	quantity = int(input("item (enter \"done\" when finished): "))

	item = {
		"name" : item_name,
		"price": price,
		"quantity": quantity
	}
	
	list_of_items.append(item)

print("-------------------")
print("receipt")
print("-------------------")

total = 0
for item in list_of_items:
	print("%s %s %sKD" %(item["quantity"], item["name"], item["price"]*item["quantity"]))
	total = total + item["quantity"] * item["price"]

print("-------------------")
print("Total: %s KD" %total)
# cart = {
# 	"apples" : .2,
# 	"carrot" : .1,
# 	"flour" : 1.3,
# 	"water_bottles" : .05
# }
# for keys in cart:
# 	print("""
# 	item (enter "done" when finished): apples
# 	price: .2
# 	quantity: %s
# 	item (enter "done" when finished): carrot
# 	price: .1
# 	quantity: %s
# 	item (enter "done" when finished): flour
# 	price: 1.3
# 	quantity: %s
# 	item (enter "done" when finished): water bottles
# 	price: .05
# 	quantity: %s
# 	item (enter "done" when finished): done
# 	""" % (apples, carrot, flour, water_bottles))
# 	apples = input("apples: ")
# 	carrot = input("carrot: ")
# 	flour = input("flour: ")
# 	water_bottles = input("water bottles: ")