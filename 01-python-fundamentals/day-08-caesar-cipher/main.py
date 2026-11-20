#caesar cipher
alphabet = [
    ' ', 
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',

    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',

    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',

    '!', '"', '#', '$', '%', '&', "'", '(', ')',
    '*', '+', ',', '-', '.', '/', ':', ';', '<', '=',
    '>', '?', '@', '[', '\\', ']', '^', '_', '`',
    '{', '|', '}', '~'
]

decider=input('type encode or decode encrypt?\n').lower()
text=input("type your message\n").lower() 
shift=int(input("type the shift number\n"))
#one way to do it is by using the for loop and while loop and if else statement
# message=""
# index=0
# counter=0
# if decider=="decode":
#     for char in text:
#         if char!=" ":
#             while char!=alphabet[index]:
#                 index+=1
#             if(index-shift)<0:
#                 message=message+alphabet[len(alphabet)+(index-shift)]
#             else:
#                 message=message+ alphabet[index-shift]
#             index=0

#         else:
#             message= message+ ' '
#     print(message)
# elif decider=="encode":
#     for word in text:
#         if word!=" ":
#             while word!= alphabet[counter]:
#                 counter+=1
            
#             if (counter+shift)>=len(alphabet):
#                 message=message+alphabet[(counter+shift)%len(alphabet)]
#             else:
#                 message=message+alphabet[(counter+shift)]
#             counter=0
#         else:
#             message= message+ ' '
#     print(message)
# else:
#     print ("wrong input!!!")
    


#another way to do it is by using the function and index function of the list
def caesar(input_text, shift_amount, cipher_direction):
    output_text = ""
    for char in input_text:
        if char in alphabet:
            position = alphabet.index(char)
            if cipher_direction == "encode":
                new_position = (position + shift_amount) % len(alphabet)
            elif cipher_direction == "decode":
                new_position = (position - shift_amount) % len(alphabet)
            output_text += alphabet[new_position]
        else:
            output_text += char
    print(f"The {cipher_direction}d text is: {output_text}")
    
caesar(input_text=text, shift_amount=shift, cipher_direction=decider)