def list_sum(list_of_numbers):
    return sum(set(list_of_numbers))

if __name__ == "__main__":
    print(list_sum([12,14,5,9]))
    print(list_sum([1,2,3,4]))
    print(list_sum([5,5,1,2,3,4]))
