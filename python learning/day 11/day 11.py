import random
def picked_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    choice_card=random.choice(cards)
    return choice_card

def calc_score(card):
    """ Take a list of cards and return the sum of list

    Args:
        card (List): a list of cards

    Returns:
        int: sum list of cards
    """
    if sum(card)==21 and len(card)==2:
        return 0
    if 11 in card and sum(card)>21:
        card.remove(11)
        card.append(1)
    return sum(card)

def compare(u_score,c_score):
    if u_score== c_score:
        return "draw"
    elif u_score==0:
        return "win with a blackjack"
    elif c_score==0:
        return "lose , opponent has blackjack"
    elif u_score > 21 :
        return "you went over , you lose"
    elif c_score > 21:
        return " opponent went over , you win"
    elif u_score > c_score:
        return "you win "
    else:
        return "you lose "
    
    
def play_game():
    user_card=[]
    computer_card=[]
    is_game_over=False
    computer_score=-1
    user_score=-1


    for i in range (2):
        user_card.append(picked_card())
        computer_card.append(picked_card())

    while not is_game_over:   
        user_score=calc_score(user_card)
        computer_score=calc_score(computer_card)
        print(f"your cards: {user_card} , current score: {user_score}")
        print(f"computer's first cards : {computer_card[0]}")

        if user_score ==0 or computer_score == 0 or user_score > 21:
            is_game_over=True
        else:
            user_should_deal=input("Type 'y' to get another card, type 'n' to pass\n")
            if user_should_deal== "y":
                user_card.append(picked_card())
            else:
                is_game_over=True

    while computer_score !=0 and computer_score < 17 :
        computer_card.append(picked_card())
        computer_score=calc_score(computer_card)

    print(f"your final hand : {user_card}, final score {user_score}")    
    print(f"computer's final hand : {computer_card} , final score : {computer_score}")
    print(compare(u_score=user_score,c_score=computer_score))

while input("do you want to play a game of blackjack? type 'y' or 'n'\n")=="y":
    play_game()