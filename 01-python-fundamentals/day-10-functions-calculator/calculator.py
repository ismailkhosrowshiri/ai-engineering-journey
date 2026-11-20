def calculator(first_number,operator,second_number):
    """_summary_

    Args:
        first_number (float): first number or result
        operator (string): operator for calculating
        second_number (float): second number for doing calculate

    Returns:
        float: result of the calculator
    """
    if operator== "+":
        return first_number + second_number
    elif operator== "-":
        return first_number - second_number
    elif operator== "/":
        return first_number / second_number
    elif operator == "*":
        return first_number * second_number
    else:
        return "wrong operator selected"

first_num=float(input('type your first number\n'))
operator_num=input("select your operator\n'+'\n'-'\n'*'\n'/'\n").lower()
second_num=float(input("type your second number\n"))
result=0
result=calculator(first_number=first_num,operator=operator_num,second_number=second_num)
print(result)
continue_calc=True

while continue_calc:
    continue_with_result=input(f"type 'y' to continue with {result} , or type 'n' to start new calculation\n")
    
    if continue_with_result== "y":
        operator_num=input("select your operator\n'+'\n'-'\n'*'\n'/'\n").lower()
        second_num=float(input("type your second number\n"))
        first_num=result
        result=calculator(first_number=first_num,operator=operator_num,second_number=second_num)
    elif continue_with_result=="n":
        first_num=float(input('type your first number\n'))
        operator_num=input("select your operator\n'+'\n'-'\n'*'\n'/'\n").lower()
        second_num=float(input("type your second number\n"))
        result=0
        result=calculator(first_number=first_num,operator=operator_num,second_number=second_num)
    continue_calculating=print(input("do you wanna use from calculator if you wanna type yes or not type no")).lower()
    if continue_calculating== "no":
        continue_calc=False


#another way to  create calculator
def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply (n1,n2):
    return n1 * n2
def divide (n1,n2):
    return n1 /n2
 
operators={"+":add,"-":subtract,"*":multiply,"/":divide}
def calc():
    should_accumulate=True
    num1=float(input("input your first number\n"))

    while should_accumulate:
        op_symbols_input=input("pick an operation \n")
        for symbols in operators:
            print(symbols)    
        num2=float(input("input your second number\n"))
        answer=operators[op_symbols_input](n1=num1,n2=Num2)
        print(f"{num1} {op_symbols_input} {num2} = {answer}")
        choice=input(f"type 'y' to continue calculating with {answer} or type 'n' to start a new calculation")
        if choice=="y":
            num1=answer
        elif choice=="n":
            should_accumulate=False
            calc()
calc()