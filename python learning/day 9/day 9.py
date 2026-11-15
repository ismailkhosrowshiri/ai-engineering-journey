#dictionary and nested dictionary and list
dictionary={"hello":"world","name":"ismail","lastName":"khosrowshiri"}
#for printing dictionary
print(dictionary["hello"])
#for adding another key and value to dictionary
dictionary["whats"]="weather"
print(dictionary)
#empty dictionary
number={1:"one",2:"two",3:"three"}
print(number)
number={}
print(number)
#editing a specific key value
dictionary["hello"]="you"
print(dictionary)
#loop through a dictionary
for key in dictionary:
    #print key = printing "hello","name","lastName"
    print(key)
    #for printing key value 
    print(dictionary[key])


#nesting a dictionary
travel={"fars":["shiraz","zarghan","amrvdasht"],"khorasan_razavi":["mashhad","sabzevar"]}
print(travel)
#for access to key value
print(travel["fars"][1])
#nesting a list
character=["a","b",["c","d"]]
print(character)
#for access to nesting value in list
print(character[2][1])

#nesting dictionary in dictionary
travel_log={
"fars":{
    "city":["shiraz","zarghan","marvdasht"],
    "total_visited":"5"},
"khorasan_razavi":{
    "city":["mashhad","sabzevar"],
    "total_visited":"10"
}}
print(travel_log)

#for access to fars all info
print(travel_log["fars"])
#for access to fars city value
print(travel_log["fars"]["city"])
#for access to fars city specific city == shiraz
print(travel_log["fars"]["city"][0])

#bidder project
bidder_name=input("whats the bidder name \n")
bidder_price=int(input("how much do you bid? $\n"))
bids[bidder_name]=bidder_price
should_continue=input("Are they another bidder ? type yes or no\n").lower

continue_bidding=True
while continue_bidding:
    bidder_name=input("whats the bidder name \n")
    bidder_price=int(input("how much do you bid? $\n"))
    bids[bidder_name]=bidder_price
    should_continue=input("Are they another bidder ? type yes or no\n").lower
    if should_continue== "no":
        continue_bidding=False
        bidding_function(bids)
    elif should_continue=="yes":
        print("\n"*100)
        
        
        
def bidding_function(bid_dic):
    winner=''
    max_bid =0
    for bidder in bid_dic:
        bid_amount=bids[bidder]
        if bid_amount>max_bid:
            max_bid=bid_amount
            winner=bidder
    print(f"the winner is {winner} and the with a bid of ${max_bid}")
    
    
#max function in dictionary
print(max(bids),key=bids.get)