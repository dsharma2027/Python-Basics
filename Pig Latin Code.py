#Pig Latin Code
def pig_latin(mystr):
    pig_word = ''
    for i in mystr.split():
        first_letter = i[0]
        if first_letter.lower() in 'aeiou':
            pig_word = pig_word + i + 'ay '
        else:
             pig_word = pig_word + i[1:] + first_letter + 'ay '
    return pig_word
code = input("Please enter the Code: ")
code1 = pig_latin(code)
print('The message is: {}' .format(code1))
