def alphabet_position(letter):
    if letter.isupper():
        return (ord(letter) - 65)  # convert character to integer using ASCII code
    else:
        return (ord(letter) - 97)


def rotate_character(char, rot):
    pos = (alphabet_position(char) + rot) % 26
    new_char = chr(pos + 65)  # convert to character using the ASCII code
    if char.islower():  # preserve the case of the character being rotated
        new_char = new_char.lower()
    return new_char


def rotate_string(text, rot):
    cipher = ''
    for i in text:
        if i.isalpha():  # If the character is a alphabet then only rotate it otherwise leave it as it is
            cipher += rotate_character(i, rot)
        else:
            cipher += i
    return cipher


def main():
    text = input( "Type a message: \n")
    rot = input( "Rotate by: \n")
    rot = int(rot)  # Since raw_input return a string, therefore type cast to integer
    print(rotate_string(text, rot))

if __name__ == "__main__":
    main()