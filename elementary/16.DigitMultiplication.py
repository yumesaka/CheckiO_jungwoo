def checkio(number: int) -> int:
    number_list = []

    quotient =1
    mod = 0

    while quotient > 0:
        quotient, mod = divmod(number, 10)
        number = quotient
        # print(quotient, ", ", mod)
        if mod != 0 :
            number_list.append(mod)

    mul = 1
    for n in number_list:
        mul = mul *n


    return mul


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")