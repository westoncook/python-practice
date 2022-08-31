def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    def dictify(lst):
        counts = {}
        for num in lst:
            if counts.get(num):
                counts[num] += 1 
            else :
                counts[num] = 1
        return counts
    
    lst1 = dictify(list(str(num1)))
    lst2 = dictify(list(str(num2)))
    return lst1 == lst2
