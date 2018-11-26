import re
def check_pangram(text):
    '''
        is the given text is a pangram.
    '''
    # your code here
    alphabet_dict = dict()
    alphabet_dict['a'] = 0
    alphabet_dict['b'] = 0
    alphabet_dict['c'] = 0
    alphabet_dict['d'] = 0
    alphabet_dict['e'] = 0
    alphabet_dict['f'] = 0
    alphabet_dict['g'] = 0
    alphabet_dict['h'] = 0
    alphabet_dict['i'] = 0
    alphabet_dict['j'] = 0
    alphabet_dict['k'] = 0
    alphabet_dict['l'] = 0
    alphabet_dict['m'] = 0
    alphabet_dict['n'] = 0
    alphabet_dict['o'] = 0
    alphabet_dict['p'] = 0
    alphabet_dict['q'] = 0
    alphabet_dict['r'] = 0
    alphabet_dict['s'] = 0
    alphabet_dict['t'] = 0
    alphabet_dict['u'] = 0
    alphabet_dict['v'] = 0
    alphabet_dict['w'] = 0
    alphabet_dict['x'] = 0
    alphabet_dict['y'] = 0
    alphabet_dict['z'] = 0

    for charactor in text:
        if charactor.isalpha():
            alphabet_dict[charactor.lower()] += 1

    for key, value in alphabet_dict.items():
        if value == 0:
            return False
    return True

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
    print('If it is done - it is Done. Go Check is NOW!')