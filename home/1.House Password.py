import re
def checkio(data: str) -> bool:

    #replace this for solution
    res = False
    if len(data) >= 10:
        res = True
    else:
        return False
    
    if re.search('[0-9a-zA-Z]', data) ==None:
        return False

    if re.search('[0-9]', data) == None:
        return False

    if re.search('[a-z]', data) == None:
        return False

    if re.search('[A-Z]', data) == None:
        return False

    return True

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")