def checkio(number):
    pidgeons=0
    i=1
    while True:
        if number<=pidgeons:
            return pidgeons
        pidgeons+=i
        if number<pidgeons:
            return number
        number-=pidgeons
        i+=1


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
    print(checkio(18))