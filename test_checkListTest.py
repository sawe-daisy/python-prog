from checkList import checkList

def test_checkListTest():
    # test for valid input
    inputValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 36, 44, 51, 46, 77, 98, 99, 10]
    assert checkList(inputValues) == [2, 6, 8, 15, 44, 98, 10]

    # test Valid length
    inputValues = [11, 15, 36, 44, 51, 46, 77, 98, 99]
    assert checkList(inputValues) is None

    # test list with multiples of 2 and 3 removed
    inputValues = [11, 15, 36, 44, 51, 46, 77, 98, 99, 100]
    assert checkList(inputValues) == [15, 46, 98]

    # test for negative values
    inputValues = [-11, -15, -36, -44, -51, -46, -77, -98, -99, -100]
    assert checkList(inputValues) == [-15, -46, -98]

if __name__ == "__main__":
    test_checkListTest()