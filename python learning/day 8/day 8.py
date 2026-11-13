#caesar cipher
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z',]
decider=input('type encode or decode encrypt?\n').lower()
text=input("type your message\n").lower() 
shift=int(input("type the shift number\n"))
message=""
index=0
counter=0
if decider=="decode":
    for char in text:
        if char!=" ":
            while char!=alphabet[index]:
                index+=1
            if(index-shift)<0:
                message=message+alphabet[26+(index-shift)]
            else:
                message=message+ alphabet[index-shift]
            index=0

        else:
            message= message+ ' '
    print(message)
elif decider=="encode":
    for word in text:
        if word!=" ":
            while word!= alphabet[counter]:
                counter+=1
            
            if (counter+shift)>=26:
                message=message+alphabet[(counter+shift%26)]
            else:
                message=message+alphabet[(counter+shift)]
            counter=0
        else:
            message= message+ ' '
    print(message)
else:
    print ("wrong input!!!")
    


#another way to do it is by using the function and index function of the list
def caesar(input_text, shift_amount, cipher_direction):
    output_text = ""
    for char in input_text:
        if char in alphabet:
            position = alphabet.index(char)
            if cipher_direction == "encode":
                new_position = (position + shift_amount) % 26
            elif cipher_direction == "decode":
                new_position = (position - shift_amount) % 26
            output_text += alphabet[new_position]
        else:
            output_text += char
    print(f"The {cipher_direction}d text is: {output_text}")
    
caesar(input_text=text, shift_amount=shift, cipher_direction=decider)