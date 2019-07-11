import time

#Degree to Radian
Deg=32
ans=Deg*(3.141592653589793/180)
print (ans)


#Calculating Surface Area and Volume of Sphere
radius=input('Enter your radius')
Sarea=4*3.141592653589793*radius*radius
vol=(4/3)*3.141592653589793*radius*radius
print ('Surface Area is ', Sarea)
print ('And Volume is ', vol)  

#Time
localtime = time.asctime( time.localtime(time.time()) )
print ("The time is :", localtime)

#Splitting Strings
name = "My name is Michael Essien"
a = name.split()
print (a)

#Joining List
name = ['Michael', 'is', 'a', 'boy']
age = ['i', 'am', '22', 'years', 'old']
print (name + age)
print (name.extend(age))

