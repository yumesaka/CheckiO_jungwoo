def popular_words(text: str, words: list) -> dict:
    # your code here
    low_text = text.lower()
    list_low_text = low_text.split()
    word_dict = {}
    for word in words:
        word_count = 0

        for origin_word in list_low_text:
            if origin_word == word:
                word_count += 1

        word_dict[word] = word_count

    return word_dict


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")