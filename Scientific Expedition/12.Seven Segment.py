segment_0_9 = dict()
segment_0_9[0] = [1, 1, 1, 1, 1, 1, 0]
segment_0_9[1] = [0, 1, 1, 0, 0, 0, 0]
segment_0_9[2] = [1, 1, 0, 1, 1, 0, 1]
segment_0_9[3] = [1, 1, 1, 1, 0, 0, 1]
segment_0_9[4] = [0, 1, 1, 0, 0, 1, 1]
segment_0_9[5] = [1, 0, 1, 1, 0, 1, 1]
segment_0_9[6] = [1, 0, 1, 1, 1, 1, 1]
segment_0_9[7] = [1, 1, 1, 0, 0, 0, 0]
segment_0_9[8] = [1, 1, 1, 1, 1, 1, 1]
segment_0_9[9] = [1, 1, 1, 1, 0, 1, 1]


def splitToIndex(lit_seg):
    first_seg = set()
    second_seg = set()

    for lit_element in lit_seg:
        if lit_element.islower():
            second_seg.add(ord(lit_element.upper()) - ord('A'))
        else:
            first_seg.add(ord(lit_element) - ord('A'))

    return first_seg, second_seg

def get_pred_segment(lit_seg, broken_seg):
    pred_segment = []
    for key in segment_0_9.keys():
        temp = segment_0_9[key].copy()
        for i in lit_seg:
            temp[i] -= 1
        if -1 in temp:
            continue
        for j in broken_seg:
            temp[j] -= 1
        if not 1 in temp:
            pred_segment.append(key)

    return pred_segment


def seven_segment(lit_seg, broken_seg):
    first_seg, second_seg = splitToIndex(lit_seg)
    first_broken_seg, second_broken_seq = splitToIndex(broken_seg)

    pred_first = get_pred_segment(first_seg,first_broken_seg)
    pred_second = get_pred_segment(second_seg,second_broken_seq)

    pred_list = set()
    for number in pred_first:
        for number2 in pred_second:
            pred_num = str(number) + str(number2)
            pred_list.add(pred_num)

    # replace this for solution
    print(len(pred_list))
    print(sorted(pred_list))
    return len(pred_list)


if __name__ == '__main__':
    assert seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2, '11, 71'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}) == 6, '15, 16, 35, 36, 75, 76'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}) == 20, '15...98'
    print('"Run" is good. How is "Check"?')
