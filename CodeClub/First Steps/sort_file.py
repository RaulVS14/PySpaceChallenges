from functools import wraps


def check_args(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if len(args) > 1:
            raise TypeError("Incorrect usage of function")
        return func(*args, **kwargs)

    return inner


@check_args
def sort_file(csv, insep=",", inend="\n", outsep=",", outend="\n"):
    rows = csv.split(inend)
    filter_data = list(filter(lambda row: "#" not in row and row != '', rows))
    data = [row.split(insep) for row in filter_data]
    sorted_data = sorted(data)
    return outend.join([outsep.join(row) for row in sorted_data])


if __name__ == "__main__":
    try:
        sort_file("abc", "file")
    except TypeError as exc:
        print(exc)

    # A string with only one item per row
    assert sort_file('b\ny\na') == 'a\nb\ny'

    # Providing some keyword arguments
    assert sort_file('b,b\ny,y\na,a', outsep=':', outend='\t') == 'a:a\tb:b\ty:y'

    # Blank lines and lines starting with '#' should not appear in the result
    assert sort_file('b,q\n\n#p,y\na,o', outsep='-') == 'a-o\nb-q'

    # Proper sorting and ignore blank lines at the end
    assert sort_file('2,3,d\n2,4,x\n2,4,a\n\n\n', outend=' -- end\n') == '2,3,d -- end\n2,4,a -- end\n2,4,x'
