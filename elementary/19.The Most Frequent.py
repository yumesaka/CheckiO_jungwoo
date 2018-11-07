# def most_frequent(data: list) -> str:
#     """
#         determines the most frequently occurring string in the sequence.
#     """
#     # your code here
#     dict_word ={}
#     for element in data:
#         dict_word[element] = data.count(element)
#
#     return max(dict_word, key=dict_word.get)

def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    # your code here

    return max(data, key=data.count)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print('Example:')
    print(most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]))

    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')

