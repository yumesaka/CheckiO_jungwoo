def sun_angle(time):
    #replace this for solution
    hour, min =  time.split(":")
    hour = int(hour)
    min = int(min)

    if (hour >= 18 and min > 0) or (hour < 6) :
        print("I don't see the sun!")
        return "I don't see the sun!"
    convert_min = hour * 60 + min
    convert_min = convert_min - (6 * 60) #6시를 0으로 기준을 세움
    degree = 180 * (convert_min / (12*60))

    return degree

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")

