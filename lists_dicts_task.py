skills = ["Food", "Video Games", "Rock","Roll","KungFu"]
cv = {}
print("Welcome to the special recruitment program, please answer the following questions: ")
cv["name "] = input("name: ")
cv["age "] = int(input("age: "))
cv["experience "] = int(input("how many years of experience do you have? "))
cv["skills"] = []
for items in skills:
	print (skills.index(items)+1, items)

cv["first_skill"] = input("choose a skill from above: ")
cv["second_skill"] = input("choose another skill from above: ")

if cv["age "] >= 17 and cv ["age "] < 55 and cv["first_skill"].count("Food") > 0:
	print ("you have beem accepted, %s" % cv["name "])
else:
	print("sorry not sorry!")