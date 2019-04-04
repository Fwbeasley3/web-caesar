def alphabet_position(letter):
    if letter.isupper():
        return (ord(letter)-65)     
    else:
        return (ord(letter)-97)
def rotate_character(char,rot):
    pos = (alphabet_position(char)+rot)%26
    new_char = chr(pos+65)          
    if char.islower():             
        new_char = new_char.lower()
    return new_char