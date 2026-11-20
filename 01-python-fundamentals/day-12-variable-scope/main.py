#scoping global var and local
#in function var is local and in if while or for create a var is a global var
#you cant use var create in function in outside of function
#the way can modify a global var using a global word in function .
#dont recommend use global key
#hello = "hi"
# def hi ():
#global hello
#     hello="hello "
# print (hi())

#print(hello)   # you cant use hello like this local var

# you can use like this 

def hi ():
    hello="hello"
    return hello
print(hi()) 

        
    


