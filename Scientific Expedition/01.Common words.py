def checkio(first, second):
    first_word_list = first.split(",")
    second_word_list = second.split(",")

    match_word_list = []
    for first_word in first_word_list:
        for second_word in second_word_list:
            if first_word == second_word:
                match_word_list.append(first_word)

    res = ""
    match_word_list.sort()
    if len(match_word_list) > 0:
        res = ",".join(match_word_list)
    else:
        res = ""

    return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
