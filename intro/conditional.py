i=8
if(i%2==0):
	print("Even Number")
else:
	print("Odd Number")

#% stands for modulo. i%2 is 0

def evens():
	list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	if (list%2==0):
		print(list)
	else:
		print("none")
evens()

#Person Age
def age():
	person_age=int(input("Please enter your age: "))
	if person_age < 18:
		print("You are young")
	else:
		print("You are old")
age()

#Person Year
def year():
	person_year=int(input("Enter year you were born: "))

	while (person_year <1900|| person_year>2019):
		person_year=int(input("Wrong input, Retype :"))

	if person_year>1900 & person_age<2019:
		years=2019-person_year
		print("You are ", years, " old")
year()

#Leap Year
def leap_year()
	
leap_year()
