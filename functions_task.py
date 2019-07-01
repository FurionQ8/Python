import datetime
from dateutil.relativedelta import relativedelta
d = datetime.date(int(input("Enter year of birth: ")),int(input("Enter month of birth: ")),int(input("Enter day of birth: ")))

def check_birthday(d):
	if d > datetime.date.today():
		print("birthdate is invalid.")
	else:
		return True

def calculate_age(d):
	if check_birthday(d) == True:
		tdy = datetime.date.today()
		rdelta= relativedelta(tdy, d)
		print ("you are %s years, %s months, and %s days" % (rdelta.years, rdelta.months, rdelta.days))

calculate_age(d)