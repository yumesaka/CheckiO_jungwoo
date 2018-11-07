import re
def find_message(text: str) -> str:
    """Find a secret message"""

    p = re.compile('[A-Z]')
    finded_list = p.findall(text)

    return ''.join(finded_list)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
