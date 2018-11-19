def checkio():
    i = 16

    in_hex_has_only_1_and_0 = not bool(set(hex(i)[2:]) - set('01'))

    oct_twice_bigger_than_hex_in_10_radix = int(oct(i)[2:]) / int(hex(i)[2:]) == 2.0

    convert_to_hex_to_str_give_two_in_bin = int(hex(i)[2:], 2)

    count_of_0_in_4_times = bin(i)[2:].count('0') / hex(i)[2:].count('0')

    and_2_in_power_4_give_stil_16 = 2 ** count_of_0_in_4_times

    best_number = (
        in_hex_has_only_1_and_0 and
        oct_twice_bigger_than_hex_in_10_radix and
        convert_to_hex_to_str_give_two_in_bin and
        count_of_0_in_4_times == 4 and
        and_2_in_power_4_give_stil_16 == 16
    )

    if best_number:
        return i


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(checkio(), (int, float, complex))