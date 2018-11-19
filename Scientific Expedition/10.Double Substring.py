def double_substring(line):
    sameword_list = []
    for i in range(len(line)-1):
        for j in range(i, len(line)):
            if line[i:j] in line[j:]:
                sameword_list.append(line[i:j])

    if len(sameword_list) >0 :
        print(max(sameword_list, key=len))
        return len(max(sameword_list, key= len))
    else:
        return 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    print('"Run" is good. How is "Check"?')