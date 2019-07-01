print("Welcome to the special recruitment program, please answer the following questions: ")
skills = ["Netflix", "Video Games", "Rock", "Roll", "cate"]
cv = {}

name = input("name: ")
cv["name "] = name 

cv["age "] = int(input("age: "))
cv["experience "] = int(input("how many years of experience do you have? "))
cv["skills"] = []

for items in skills:
	print (skills.index(items)+1, items)
""" the teacher listed each one on its's own: print("1. %s" % skills[0])) """
first_skill = input("choose a skill from above: ")
cv["skills"].append(skills[int(skill1)-1])
""" we put the minus sign to adjust the index"""
second_skill = input("choose another skill from above: ")
cv["skills"].append(skills[int(skill2)-1])

if cv["age"] >= 17 and cv ["age"] < 50 and cv["skills"][0] == skill [2] or cv["skills"][1] == skill[1]:
	print ("you have beem accepted, %s" % cv["name"])
else:
	print("fuck off!")