import re

class HackerLanguage:

    def __init__(self):
        self.binary_str_list = []
        self.str_list = []

    def write(self, message):
        # binary_str_list = []
        for character in message:
            self.str_list.append(character)
            if character == " ":
                self.binary_str_list.append("1000000")
            elif re.match("[0-9.:!?@$%]", character) != None:
                self.binary_str_list.append(character)
            else:
                convert_ascii = bin(ord(character)).replace("0b", "")
                self.binary_str_list.append(convert_ascii)

    def delete(self, remove_size):
        self.binary_str_list =  self.binary_str_list[ : -1* remove_size]
        self.str_list =  self.str_list[ : -1* remove_size]

    def send(self):
        return "".join(self.binary_str_list)


    def read(self, binary_str):
        binary_str_list =[]
        i = 0
        while len(binary_str) > i:
            if re.match("[.:!?@$%]", binary_str[i]) != None:
                binary_str_list.append(binary_str[i])
                i = i + 1
            else:
                encode_str = binary_str[i: i + 7]
                if encode_str == "1000000":
                    encode_str = "100000"
                decode_chr = chr(int(encode_str,2))
                if re.match("[a-zA-Z\s]", decode_chr) != None:
                    binary_str_list.append(decode_chr)
                    i = i +7
                else:
                    binary_str_list.append(binary_str_list[i])
                    i = i + 1

            # if re.match("[2-9:.:!?@$%]", binary_str[i]) != None:
            #     binary_str_list.append(binary_str[i])
            #     i = i+1
            # else:
            #     encode_str =  binary_str[i: i + 7]
            #     decode_chr = chr(int(encode_str,2))
            #     binary_str_list.append(decode_chr)
            #     i = i+7

        decode_str = "".join(binary_str_list)
        print(decode_str)
        return decode_str

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    message_1 = HackerLanguage()
    message_1.write("secrit")
    message_1.delete(2)
    message_1.write("et")
    message_2 = HackerLanguage()

    assert message_1.send() == "111001111001011100011111001011001011110100"
    assert message_2.read("11001011101101110000111010011101100") == "email"
    print("Coding complete? Let's try tests!")
