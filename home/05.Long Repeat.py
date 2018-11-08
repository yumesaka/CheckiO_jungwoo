def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    if len(line) == 0:
        return 0
    repeat_list = []
    start_index = 0
    for i in range(1, len(line)):
        if line[i] != line[i - 1]:
            repeat_list.append(line[start_index: i])
            start_index = i

    if len(repeat_list) == 0:
        repeat_list.append(line)
    # print(repeat_list)

    return len(max(repeat_list, key=len))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
