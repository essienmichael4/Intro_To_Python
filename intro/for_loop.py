for i in range(1,11):
    print (i)
#the code is iterating through 1 to 11
#i  is an int varible and range is a function 

for j in [1, 2, 3]:
    print (j)
#The code is iterating through the list J

#Using Range
for j in range(1,3):
    print (j)

#Type is a list
#Range returns integer


#Stars
def set():
    J = 1
    while (J < 5):
        print ("****")
        J+=1
set()


def star():
    for i in range(0, 4):
        for a in range (0, i+1):
            print ("*", end="")
        print()
    for i in reversed(range(0, 4)):
        for a in range (0, i+1):
            print ("*", end="")
        print()
        
star()

#Function String=True/False

def string():
    letters=input('Enter any word')
    for letter