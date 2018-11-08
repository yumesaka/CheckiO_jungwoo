def to_encrypt(text, delta):
    #replace this for solution
    char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # encrypt_list = []
    encrypt_str = ''
    for i in range(len(text)):
        if text[i] == ' ':
            # encrypt_list.append(' ')
            encrypt_str += ' '
        else:
            # encrypt_list.append(
            #     char_list[  ord(text[i]) - ord('a') + delta ]
            # )
            index = ord(text[i]) - ord('a') + delta
            index = index % len(char_list)
            encrypt_str += char_list[index]
    return encrypt_str

if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")