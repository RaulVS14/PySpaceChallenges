def is_fibonacci(n):
    a = 0
    b = 1
    while a <= n:
        if n == a:
            return True
        a, b = b, a + b
    return False

def fibonacci_only(*args):
    sum = 0
    for i in args:
        if is_fibonacci(i):
            sum += i
    return sum

if __name__ == "__main__":
    print(fibonacci_only(1,2,3,4,5,6,7,8,9,610))
