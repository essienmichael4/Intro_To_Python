#Function to  returns even  numbers from a list
def is_even():
        numbers = [1,52,234,87,4,76,24,69,90,135]
        even = True
        x = []
        for a in numbers:
                if not a % 2 ==0:
                        x.append(a)
                        a = even
        print(x)
is_even()

