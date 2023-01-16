def swap(list_one):

    print(list_one)
    list_one[0], list_one[1], list_one[2] = list_one[2], list_one[1], list_one[0]
    print(list_one)

swap([1, 2, 3])


def rotate_left(list_one):
    """
    Given a list of ints length 3, return a list with the elements "rotated left" so [1, 2, 3] yields [2, 3, 1].
    :param list_one: A list consisting of exactly three integers
    :return: a list where all the elements have been shifted 1 place to the left
    """

    list_swapped = [6, 7, 8]
    list_swapped[0] = list_one[1]
    list_swapped[1] = list_one[2]
    list_swapped[2] = list_one[0]
    return list_swapped

print(rotate_left([1, 2, 3]))




def max_end(list_one):
    """
    This function will find if the first or last element of a list is larger, then set all the elements
    of a list to be greater than that value.
    :param list_one: A list consistig of three elements - all integers
    :return: A list where all the elements are the larger of the first or last element of the original list
    """

    list_one = [1, 2, 3]
    if list_one[0] > list_one[-1]:
        list = [list_one[0], list_one[0], list_one[0]]
        print(list_one[-1]) = [list_one(1)

    else:
        print(list_one[1, 2, 3])






