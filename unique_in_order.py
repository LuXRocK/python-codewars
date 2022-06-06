iterable = 'AAAABBBCCDAABBB'
def unique_in_order(iterable):
    result = []
    poprzednia = 0
    for i in iterable:
        if i != poprzednia:
            result.append(i)
        poprzednia = i
    return(result)
