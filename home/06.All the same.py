from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # your code here
    dummy_list = []
    for i in range(len(elements)):
        dummy_list.append(elements[0])

    return elements == dummy_list


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
