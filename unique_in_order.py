iterable = 'AAAABBBCCDAABBB'
def unique_in_order(iterable):
    result = []
    previous = 0
    for i in iterable:
        if i != previous:
            result.append(i)
        previous = i
    return(result)
