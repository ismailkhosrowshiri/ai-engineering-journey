#loop function
numbers=[1,2,5,4,5,37,3457,334,32345]
for number in numbers:
    print(number)

#sum function for summarize numbers list in python
sum_1=sum(numbers)
print (sum_1)


#other way for summarize numbers

sum_2=0
for number in numbers:
    sum_2+=number

print (sum_2)

#max function in list is showing larger number in list
print (max(numbers))

#find max number in list with for loop

max_number=0
for number in numbers:
    if max_number<number:
        max_number=number

print(max_number)

#range function in python example=  x in range (a,b)
# a=start point and include on using b= end point and not using in range
#like for number in range (1, 100) this show 1 until 99

#the gauss challenge with for and range 
total=0 
for number in range (1,101):
    total+=number
print(total)


#generate a random password with random module in python
letters = [
    'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D',
    'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H',
    'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L',
    'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P',
    'q', 'Q', 'r', 'R', 's', 'S', 't', 'T',
    'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X',
    'y', 'Y', 'z', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

user_letter=int(input("How many letters would you like in your password?\n"))
user_number=int(input("How many numbers would you like in your password?\n"))    
user_symbol=int(input("How many symbols would you like in your password?\n"))   
import random
#easy way
password=''
for letter in range (0,user_letter):
    password+=random.choice(letters)

print(password)    

for number in range (0,user_number):
    password+=random.choice(numbers)

print(password)    
 
for symbol in range (0,user_symbol):
    password+=random.choice(symbols)

print(f"Your password is: {password}")    

#hard way
password_list=[]
for letter in range (0,user_letter):
    password_list.append(random.choice(letters))

for number in range (0,user_number):
    password_list.append(random.choice(numbers))

for symbol in range (0,user_symbol):
    password_list.append(random.choice(symbols))

# random shuffle is a random function for shuffle the list
random.shuffle(password_list)
new_password=''
for char in password_list:
    new_password+=char

print(f"Your password is: {new_password}")