def checkList(inputlist):
    # check if length is divisible by 10
    if len(inputlist) % 10 != 0:
        print("Error : the length of the list is not a multiple of 10")
        return
        # filter list to remove items in position of multiples of 2 and 3
    res_list = [item for index, item in enumerate(inputlist) if index % 2 != 0 and index % 3 != 0]
    print(res_list)
    return res_list


if __name__ == "__main__":
    try:
        values = input("Enter list of numbers separated by commas : ")
        inputlist = list(map(int, values.split(",")))
    except ValueError:
        print("Kindly enter in the values in the requested format ")
        exit()

    checkList(inputlist)