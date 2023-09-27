def list_sum(list_of_numbers):
    return sum(num * num for num in list_of_numbers)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    nums2 = [1, 2, 3]
    nums3 = [2, 2, 2]
    print(list_sum(nums))
    print(list_sum(nums2))
    print(list_sum(nums3))
