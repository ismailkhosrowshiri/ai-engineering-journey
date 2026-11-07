#subscripting
#print("hello"[0])
#integer
#print(123+345)
#float Number
#print(3.14)
#boolean
#print(True)
#check type of variables
#print(type(123.1))
#change string to integer
#print(int("123")+int("456"))
#change int to string 
#print(str(123))
#sum
#print(123+456)
#min
#print(456-321)
#mul
#print(123*456)
#divine with type of float
#print(456/321)
#divine with type of int
#print(456//321)
#power
#print(3**2)
#rounding a float number
rounding_number=73/3
#print(rounding_number)
#print(round(rounding_number))
#round function have 2 argument 1 - for number 2-number of floating rounding
#print(round(rounding_number,2))
#assignment operator in python like
# point=1 point+=1  = 2 ,point -=1  = 0, point *=2 =2, point /=2 = 0.5

#calculator for bill
bill=float(input("how much is your bill\n"))
tip=int(input("how much do you give a tip 10,12,15 percent?\n"))
people=int(input("how many people to split the bill?\n"))
total_bill=round( (((( bill * tip) / 100) + bill) / people),2)
print("Each person should pay: "+ str(total_bill))