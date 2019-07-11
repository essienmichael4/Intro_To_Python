list=[]
list.append('a')
print(list)
#Line 1 creats a variable for a group of items to be stored
#Line 2 pushes a into the variable
#Line 3 prints the value 'a' in the variable

def Even_Nums_Range(min, max):
	even_num=[]
	for a in range(min, max):
		if a % 2 ==0:
			even_num.append(a)
	return even_num


print(Even_Nums_Range(1,10))
Even_numbers=Even_Nums_Range(20,30)
print(Even_numbers)
