def find_outlier(integers):
    """Return outlier from a provided list of integers"""
    even =[]
    odd =[]
    for n in integers:
        if n %2 ==0:
            even.append(n)
        else:
            odd.append(n)
    if len(even) == 1:
        outlier = even[0]
    elif len(odd) == 1:
        outlier = odd[0]
    return outlier
