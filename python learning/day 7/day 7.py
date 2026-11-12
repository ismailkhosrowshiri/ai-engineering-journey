#hangman game 
#import random
#wrong code


#word_list=['camel','blade','learning']
#word_selected=random.choice(word_list)
#dash_line=''
#for char in range(0,len(word_selected)):
#    dash_line+='_'
#    # print(len(word_list))
#
#print(dash_line)
#health=5
#right_guess=''
#
#def guess_chance():
#    user_guess=input("guess a letter!\n")
#    if user_guess in word_selected:
#        print("you guessed right!")
#        for index in range(0,len(word_selected)):
#            if word_selected[index]== user_guess:
#                dash_line=dash_line[index-1]+user_guess + dash_line[index+1]
#                right_guess=dash_line
#                if right_guess==word_selected:
#                    print("you win!!!")
#                    
#        print(dash_line) 
#    else:
#        health-=1
#    print (f"your health is {health}")
#    game()
#
#def game():
#    if health<0:
#        print("you lose! \n game over!!!")
#    else:
#        guess_chance()
#
#
#
#while right_guess==word_selected:
#    game()
#coding hangman game

import random

word_list = ['camel', 'blade', 'learning']
word_selected = random.choice(word_list)

dash_line = ['_'] * len(word_selected)

#using join function

print(' '.join(dash_line))

health = 5
right_guess = False

while health > 0 and not right_guess:

    user_guess = input("Guess a letter!\n").lower()

    if user_guess in word_selected:
        print("You guessed right!")

        for index in range(len(word_selected)):
            if word_selected[index] == user_guess:
                dash_line[index] = user_guess

        print(' '.join(dash_line))

        if '_' not in dash_line:
            right_guess = True
            print("You win!!!")

    else:
        health -= 1
        print("Wrong guess!")

    print(f"Your health is {health}")

if health == 0:
    print("You lose!")
    print(f"The word was: {word_selected}")
