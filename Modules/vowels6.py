def search_for_letters (phrase:str , letters:str="aeiou") -> set:
    """return a ser of 'letters' found in phrase """
    return set(letters).intersection(set( phrase))



print(search_for_letters ("hsggdteg","gs"))
