height=int(input("input your height? cm\n"))
#comparison operators  >= equal and bigger than , <= equal and smaller than
# == equal % give us remainder like 20%6=2
#conditional if  
#condition a=6 and = if a>2 and a<5  = false  or = if a>2 or a<5  = true
#if you have multiple string line use 3 ' in start and end of string
#if you have singe and double quotation in string use ' ""' like this
# if having string like this a= ' ali's sail "hello" ' use this ali\'s
age=int(input("input your age?\n"))
bill=0
if height>=120:
    if age<12:
        print("your height is ok for riding device and your bill is 5$")
        bill=5
    elif age<=18:
        print("your height is ok for riding device and your bill is 7$")
        bill=7
    else:
        print("your height is ok for riding device and your bill is 14$")
        bill=14
    
    photo=input("do you wanna photo? input yes or no\n")
    if photo== "yes":
        bill+=3

    print(f"your bill is {bill}")
else:
    print("your height isn't for riding device")