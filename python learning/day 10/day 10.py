#output a function
#function title is a function to change a string a first char upper case and other char to lower case
#function name
def name(f_name,l_name):
    
    #this way to document your function for other person or for you to define a function what doing
    #using """ in start text and """ in the end 
    """function title is a function to change a string a first char upper case and other char to lower case
    _summary_

    Args:
        f_name (_type_): _description_
        l_name (_type_): _description_

    Returns:
        _type_: _description_
    """
    formatted_f_name=f_name.title()
    formatted_l_name=l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(name(f_name="ismail",l_name="KHOSROW SHIRI"))