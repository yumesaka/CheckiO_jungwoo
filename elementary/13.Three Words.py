def checkio(words: str) -> bool:
    words_list = words.split()

    res = False
    cnt = 0
    for word in words_list:
        if word.isalpha():
            cnt += 1
        else:
            cnt = 0
        if cnt >= 3:
            res = True
            return res

    return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")