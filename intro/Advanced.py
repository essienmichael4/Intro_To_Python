#Function to  return true only if numbers are even
def is_even(x):
	return x % 2 == 0

is_even()

#Function to  returns even  numbers from a list
def is_even():
	numbers = [1,52,234,87,4,76,24,69,90,135]
	x = []

	for a in numbers:
		if a % 2 ==0:
			x.append(a)
	print(x)
is_even()

#Using Lambda
numbers = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]
print(list(filter(lambda a:a % 2 == 0, numbers)))

#Using Lambda
numbers = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]
print(list(filter(lambda a:a % 2 == 1, numbers)))
