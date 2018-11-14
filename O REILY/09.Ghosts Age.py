

def fibonach(n):
    i=0
    array = [0, 1]
    while array[i]+array[i+1] <= n:
        array.append(array[i]+array[i+1])
        i+=1
    return array

def is_fibonach(n):
    fibo_array = fibonach(n)
    return n in fibo_array

def checkio(opacity):
    age = 0
    new_born_opacity = 10000
    while True:

        if opacity == new_born_opacity:
            break
        age += 1
        if is_fibonach(age):
            new_born_opacity -= age
        else:
            new_born_opacity += 1

    return age



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"