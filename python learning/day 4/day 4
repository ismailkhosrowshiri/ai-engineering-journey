#import random module 
import random

#generate random integer between a and b

random_init=random.randint(1,3)
print(random_init)

#generate random float between 0 and 1 including 0 and not including 1
random_between_0_to_1=random.random()
print(random_between_0_to_1)


#generate random float between a and b and include a and b
random_uniform=random.uniform(1,10)
print(random_uniform)

#create a heads or tails game
random_heads_or_tails=random.randint(0,1)
if random_heads_or_tails==0:
    print("Heads")
else:
    print("Tails")

#list in python
my_list=["hello","world","to","you"]
#add an element to the end of the list
my_list.append("!")
print(my_list)
#add some elements to the end of the list
my_list.extend(["How","are","you?"])
print(my_list)
#add an element at a specific index
my_list.insert(2,"I am fine")
print(my_list)
#remove an element from the list
my_list.remove("I am fine")
print(my_list)
#remove an element at a specific index
my_list.pop(2)
print(my_list)
#access an element at a specific index
print(my_list[2])
#create a list 
new_list=list(("hello","how","are","you"))    
print(new_list)
#return specific element from the list
print(new_list[1:3])
#delete a item in the list 
del new_list[1]
print(new_list)

#random for select an item in the list 1 way
random_item_list= random.choice(new_list)
print (random_item_list)
# 2 way
print(new_list[random.randint(0,len(new_list))])

#create rock , scissors , paper game
user_choice=int(input("Enter your choice 0 = rock, 1 = scissors, 2 = paper: \n"))
rock_scissors_paper_list=["rock","scissors","paper"]
system_choice=random.choice(rock_scissors_paper_list)
if user_choice<0 or user_choice>2:
    print("Invalid choice\n you lose!")
elif user_choice==0 and system_choice=="scissors" :
    print("computer chose scissors\n. You win!")
elif user_choice==0 and system_choice=="paper":
    print("computer chose paper\n. You lose!")
elif user_choice==0 and system_choice=="rock":
    print("computer chose rock\n. It's a tie!")
elif user_choice==1 and system_choice=="rock":
    print("computer chose rock\n. You lose!")
elif user_choice==1 and system_choice=="scissors":
    print("computer chose scissors\n. It's a tie!")
elif user_choice==1 and system_choice=="paper":
    print("computer chose paper\n. You win!")
elif user_choice==2 and system_choice=="rock":
    print("computer chose rock\n. You win!")
elif user_choice==2 and system_choice=="scissors":
    print("computer chose scissors\n. You lose!")
elif user_choice==2 and system_choice=="paper":
    print("computer chose paper\n. It's a tie!")

#if you dont want to show the computer choice you can use this code
# if user_choice<0 or user_choice>2:
#     print("Invalid choice\n you lose!")
# elif user_choice==0 and system_choice=="scissors" or user_choice==2 and system_choice=="rock" or user_choice==1 and system_choice=="paper":
#     print(" You win!")
# elif user_choice==0 and system_choice=="paper" or user_choice==1 and system_choice=="rock" or user_choice==2 and system_choice=="scissors":
#     print(" You lose!")
# elif user_choice==0 and system_choice=="rock" or user_choice==1 and system_choice=="scissors" or user_choice==2 and system_choice=="paper":
#     print(" It's a tie!")