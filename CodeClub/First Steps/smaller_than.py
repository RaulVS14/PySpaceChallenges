def smaller_than(number_1, number_2):
    if number_1 == number_2:
        return
    if number_1 > number_2:
        result = number_2
    elif number_2 > number_1:
        result = number_1
    else:
        result = None
    return result


if __name__ == "__main__":
    print(smaller_than(1, 3))  # 1
    print(smaller_than(5, 3))  # 3
    print(smaller_than(5, 5))  # None
